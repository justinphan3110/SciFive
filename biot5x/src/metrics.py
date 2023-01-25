import sklearn.metrics
import numpy as np
from scipy.stats import pearsonr as scipy_pearsonr
import re
from datasets import load_metric

def map_name_to_metric_function(name):
  dict_ = {
    "PRF1": PRF1,
    "hoc": hoc_metric,
    "accuracy": accuracy,
    "pearsonr": pearsonr,
    'ner_metric': ner_metric,
  }
  return dict_[name]


def accuracy(targets, predictions):
  return {"accuracy": 100*sklearn.metrics.accuracy_score(targets, predictions)}

"""Functions for computing metrics.
Every function must accept a list of targets and a list of predictions and
return a dict of metrics.
Functions should assume all text inputs are unicode strings.
"""
def f1(targets, predictions, average="micro"):
  return {f"f1_{average}": 100*sklearn.metrics.f1_score(targets, predictions, average=average)}


"""
PRF1 Metric (F1 Micro) function adapt from:
https://github.com/michiyasunaga/LinkBERT/blob/main/src/seqcls/run_seqcls.py#L495
"""
def PRF1(targets, predictions):
  TP = 0
  P_total = 0
  L_total = 0
  for p,a in zip(predictions, targets):
      p = p.strip()
      a = a.strip()
      if p == a and p != "0":
          TP += 1
      if p != "0":
          P_total += 1
      if a != "0":
          L_total += 1
  P = TP / P_total if P_total else 0
  R = TP / L_total if L_total else 0
  F1 = 2 * P * R / (P + R) if (P + R) else 0
  return {"precision": P, "recall": R, "F1": F1}

"""
Metric Function for HoC adapt form:
https://github.com/michiyasunaga/LinkBERT/blob/main/src/seqcls/utils_hoc.py
"""
def divide(x, y):
    return np.true_divide(x, y, out=np.zeros_like(x, dtype=np.float), where=y != 0)

def compute_p_r_f(preds, labels):
    TP = ((preds == labels) & (preds != 0)).astype(int).sum()
    P_total = (preds != 0).astype(int).sum()
    L_total = (labels != 0).astype(int).sum()
    P  = divide(TP, P_total).mean()
    R  = divide(TP, L_total).mean()
    F1 = divide(2 * P * R, (P + R)).mean()
    return P, R, F1

def hoc_metric(targets, predictions):  
  data = {}
  label_range = [x for x in range(10)]
  for i, (p,t) in enumerate(zip(predictions, targets)):
    # catch for generated sequence that is not int id
    # print([x if not x.isditi() or int(x) not in label_range
    
    # for x in p.split('|'):
    #   if not x.isdigit() or int(x) not in label_range:
    #        print(p)
        
    p = [int(x) if x.isdigit() and int(x) in label_range else len(label_range) for x in p.split('|')]

    # label is always a correct array of label id
    t = [int(x) for x in t.split('|')]

    # if the sequence is [10] then it is an empty set()
    if len(p) == 1 and 10 in p:
      p = set()
    else:
      p = set(p)

    if len(t) == 1 and 10 in t:
      t = set()
    else:
      t = set(t)
    data[i] = (t,p)
  
  y_test = []
  y_pred = []
  for k, (true, pred) in data.items():
      t = [0] * len(label_range)
      for i in true:
          if  i >= len(label_range):
            continue
          t[i] = 1

      p = [0] * len(label_range)
      for i in pred:
          if i >= len(label_range):
            continue
          p[i] = 1

      y_test.append(t)
      y_pred.append(p)
  

  y_test = np.array(y_test)
  y_pred = np.array(y_pred)
  p, r, f1 = compute_p_r_f(y_pred, y_test)
  
  return {"precision": p, "recall": r, "F1": f1}


def pearsonr(targets, predictions):
  float_targets = [float(x) for x in targets]
  # catch score to 0.0 if return any character sequence
  for x in predictions:
    if not x.replace('.','',1).isdigit():
      print(x)
  float_predictions = [float(x) if x.replace('.','',1).isdigit() else 0.0 for x in predictions]
  
  pearsonr = float(scipy_pearsonr(float_targets, float_predictions)[0])
  return {"pearsonr": pearsonr}




def _convert_BIO_labels_NER(sequences):
    result_labels = []
    for line in sequences:
        line = re.sub(r'\*(\w+)', r'\1*', line)
        tokens = re.sub(r'[!"#$%&\'()+,-.:;<=>?@[\\]^_`{\|}~⁇]', ' ', line.strip()).split()
        seq_label = []
        start_entity = 0
        entity_type = 'O'
        for idx, token in enumerate(tokens):
            if token.endswith('*'):
                start_entity += 1 if (start_entity == 0 or token[:-1] != entity_type) else -1
                entity_type = token[:-1]
            else:
                if start_entity == 0:
                    seq_label.append('O')
                    entity_type = 'O'
                elif start_entity < 0:
                    raise "Something errors"
                else:
                    if tokens[idx - 1].endswith('*'):
                        seq_label.append('B-' + entity_type.upper())
                    else:
                        seq_label.append('I-' + entity_type.upper())

        result_labels.append(seq_label)
    return result_labels

def ner_metric(targets, predictions):
    metric = load_metric("seqeval")
    pred_labels = _convert_BIO_labels_NER(predictions)
    actual_labels = _convert_BIO_labels_NER(targets)

    for i, (a, b) in enumerate(zip(pred_labels, actual_labels)):
        len_a = len(a)
        len_b = len(b)
        
        if len_a > len_b:
            pred_labels[i] = pred_labels[i][:len_b]
        elif len_a < len_b:
            pred_labels[i] = pred_labels[i] + ['PAD'] * (len_b - len_a)
    
    results = metric.compute(predictions=pred_labels, references=actual_labels)
    return {
                "precision": results["overall_precision"],
                "recall": results["overall_recall"],
                "f1": results["overall_f1"],
                "accuracy": results["overall_accuracy"],
            }