# BioT5X: Pretrained T5X Transformer for Biomedical Text Generation and Classification 

In-Progress Work

BioT5X: Pretrained T5X Transformer for Biomedical Text Generation and Classification 


| Model           |    Size     | Step | Config  | Checkpoint  |
|:---------------:|:-----------:|:----:|:-------:|:-----------:|
| BioT5X    | base & large  | 1200000 | [T5_1_0 configs](https://github.com/justinphan3110/BioT5X/tree/main/configs/t5/t5_1_0)| `gs://scifive/biot5x/pubmed_pmc/{size}/ biot5x_pubmed_pmc_{size}/` |

## Finetune
```[python]
model_size = 'base'
task = 'HoC'
train_file = f'BioT5X/data/{task}/train_blurb.tsv'
test_file = f'BioT5X/data/{task}/test_blurb.tsv'

model_dir = f'out/{task}/{model_size}_{task}_1'
pretrained_path=f'biot5x_pubmed_pmc_{model_size}/{model_size}'
gin_file = f'BioT5X/configs/biot5x/finetune/base/{task}_blurb.gin'


eval_period = 50
metric = 'hoc'

%run 'BioT5X/src/finetune_biot5x.py' \
  --gin_file="{gin_file}" \
  --gin.MODEL_DIR="'{model_dir}'" \
  --gin.EVAL_PERIOD='{eval_period}'\
  --gin.INITIAL_CHECKPOINT_PATH="'{pretrained_path}'" \
  --task="{task}" \
  --metric="{metric}" \
  --train_file="{train_file}" \
  --predict_file="{test_file}"
```

## Results

### BLURB (Classification)
|           Task          | PubmedBERT<sub>base</sub> | BioLinkBERT<sub>base</sub> | **BioT5X<sub>base</sub>** |
|:-----------------------:|-----------------|------------------|-----------------|
| <sub>**Relation Extraction**</sub>                                     
| Chemprot                |      77.24      |       77.57      |    **77.40**    |
| GAD                     |      82.34      |       84.39      |    **83.66**    |
| DDI                     |      82.36      |       82.72      |    **82.63**    |
| <sub>**Document classification**</sub>
| HoC                     |      82.32      |       84.35      |    **82.39**    |
| <sub>**Question answering**</sub>
| BioASQ                  |      87.56      |       91.43      |    **91.43**    |
| PubMedQA                |      55.84      |       70.20      |    **67.60**    |

