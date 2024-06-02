# SciFive

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/named-entity-recognition-on-bc5cdr-chemical)](https://paperswithcode.com/sota/named-entity-recognition-on-bc5cdr-chemical?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/relation-extraction-on-chemprot)](https://paperswithcode.com/sota/relation-extraction-on-chemprot?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/natural-language-inference-on-mednli)](https://paperswithcode.com/sota/natural-language-inference-on-mednli?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/named-entity-recognition-on-species-800)](https://paperswithcode.com/sota/named-entity-recognition-on-species-800?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/named-entity-recognition-on-bc5cdr-disease)](https://paperswithcode.com/sota/named-entity-recognition-on-bc5cdr-disease?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/drug-drug-interaction-extraction-on-ddi)](https://paperswithcode.com/sota/drug-drug-interaction-extraction-on-ddi?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/document-classification-on-hoc)](https://paperswithcode.com/sota/document-classification-on-hoc?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/named-entity-recognition-ner-on-ncbi-disease)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-ncbi-disease?p=scifive-a-text-to-text-transformer-model-for)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/scifive-a-text-to-text-transformer-model-for/named-entity-recognition-ner-on-jnlpba)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-jnlpba?p=scifive-a-text-to-text-transformer-model-for)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![arXiv](https://img.shields.io/badge/arXiv-2106.03598-b31b1b.svg)](https://arxiv.org/abs/2106.03598)

SciFive provided a Text-Text framework for biomedical language and natural language in NLP. Under the [T5](https://github.com/google-research/text-to-text-transfer-transformer)'s framework and desrbibed in the paper [SciFive: a text-to-text transformer model for biomedical literature](https://arxiv.org/abs/2106.03598), SciFive achieve state-of-the-art and competitive results on multiple biomedical-natural language tasks. 


# 🎉 UPDATE Jan 2023
## We are migrating SciFive into [BioT5X: Pretrained T5X Transformer for Biomedical Text Generation and Classification](https://github.com/justinphan3110/SciFive/tree/main/biot5x) that use [T5X](https://github.com/google-research/t5x) and [Flaxformer](https://github.com/google/flaxformer)

###  📝 Our example BioT5X Fine-tunning notebook for the BLURB Tasks [finetunning_biot5x_blurb.ipynb](https://github.com/justinphan3110/SciFive/blob/main/biot5x/examples/finetunning_biot5x_blurb.ipynb)


# 🤗 HuggingFace
* **SciFive Pubmed+PMC**: [Base](https://huggingface.co/razent/SciFive-base-Pubmed_PMC) | [Large](https://huggingface.co/razent/SciFive-large-Pubmed_PMC) 
* **SciFive Pubmed**: [Base](https://huggingface.co/razent/SciFive-base-Pubmed) | [Large](https://huggingface.co/razent/SciFive-large-Pubmed) 
* **SciFive PMC**: [Base](https://huggingface.co/razent/SciFive-base-PMC) | [Large](https://huggingface.co/razent/SciFive-large-PMC)

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("razent/SciFive-base-Pubmed")  
model = AutoModelForSeq2SeqLM.from_pretrained("razent/SciFive-base-Pubmed")

sentence = "Identification of APC2 , a homologue of the adenomatous polyposis coli tumour suppressor ."
text = sentence + " </s>"

encoding = tokenizer.encode_plus(text, pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")

outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    early_stopping=True
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
```


# Google Cloud Storage 

Our base Google Cloud Storage URI is at [gs://scifive]()


As described in our [paper](https://arxiv.org/abs/2106.03598), we make public 6 version of SciFive, each one has been benchmarked to achieve state-of-the-art on different biomedical task. They are all available on our [Google Cloud bucket](https://console.cloud.google.com/storage/browser/scifive), we are working on release the models on HuggingFace also.

Instruction on access Cloud Storage from the command line with python library gsutil is described [here](https://cloud.google.com/storage/docs/gsutil)

### gsutil URI for 6 SciFive models:

The following table contains pretrained SciFive checkpoints.

| Model           |    Size     | Step | Config  | Checkpoint  |
|:---------------:|:-----------:|:----:|:-------:|:-----------:|
| SciFive Pubmed    | base & large  | 1194600 & 1196500 | [T5 configs](https://storage.googleapis.com/scifive/models/pubmed/base/operative_config.gin)| `gs://scifive/models/pubmed/{size}/` |
| SciFive Pubmed+PMC    | base & large  | 1200000 | [T5 configs](https://storage.googleapis.com/scifive/models/pubmed_pmc/base/operative_config.gin)| `gs://scifive/models/pubmed_pmc/{size}/` |
| SciFive PMC    | base & large  | 1200000 | [T5 configs](https://storage.googleapis.com/scifive/models/pmc/base/operative_config.gin)| `gs://scifive/models/pmc/{size}/` |

* `{size}` is either `base` or `large`

### gsutil URI for Pretrain data:
* **Pubmed**: [gs://scifive/pretrain/pubmed]() 
* **PMC**: [gs://scifive/pretrain/pmc]() 


### Example
#### Below, we give an example of how to use SciFive on Huggingface to generate MedNLI outputs. We also publish our SciFive finetuned on MedNLI for reproducing experiments.
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("razent/SciFive-large-Pubmed_PMC-MedNLI")  
model = AutoModelForSeq2SeqLM.from_pretrained("razent/SciFive-large-Pubmed_PMC-MedNLI")
model.cuda()

sent_1 = "In the ED, initial VS revealed T 98.9, HR 73, BP 121/90, RR 15, O2 sat 98% on RA."
sent_2 = "The patient is hemodynamically stable"
text =  f"mednli: sentence1: {sent_1} sentence2: {sent_2}"

encoding = tokenizer.encode_plus(text, padding='max_length', max_length=256, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")

outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=8,
    early_stopping=True
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    print(line)
```



## Datasets

All of the finetune dataset already preprocessed into text-text format also availabe at [this](https://console.cloud.google.com/storage/browser/scifive/finetune)

## 📊&nbsp; Expected Results 


<!-- ## 🤵&nbsp; Team -->

<!--  * <b>The National Institutes of Health:</b><br/>

| James Anibal       |       Long Phan  |  Alec Peltekian | Erol Bahadiroglu |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
| <img width=120/ src="https://faes.org/sites/default/files/james_anibal.png"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4E03AQFqMmKjyQRtAQ/profile-displayphoto-shrink_400_400/0/1594192915473?e=1628726400&v=beta&t=9rPFc2GnImXXDtPoXxoS0432LjybyWJVL0b_fn6aLew"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4E03AQGIjDegQmApcQ/profile-displayphoto-shrink_200_200/0/1573082873285?e=1628121600&v=beta&t=kuXiDY3qIzmAAqDvZugOgCAcFlaGEw4fRbJf1pAdMPY"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4D03AQGygdk5u9F1HA/profile-displayphoto-shrink_200_200/0/1522727407036?e=1628121600&v=beta&t=Z_4O17wxhWnatS7Vye0VekyIJiKBMOvpdyCyO3pIaVY"> | -->

## Citations
If you use SciFive model or our code for publications, please cite: 
```
@misc{phan2021scifive,
      title={SciFive: a text-to-text transformer model for biomedical literature}, 
      author={Long N. Phan and James T. Anibal and Hieu Tran and Shaurya Chanana and Erol Bahadroglu and Alec Peltekian and Grégoire Altan-Bonnet},
      year={2021},
      eprint={2106.03598},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
