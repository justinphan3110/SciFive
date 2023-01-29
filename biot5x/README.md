# BioT5X: Pretrained T5X Transformer for Biomedical Text Generation and Classification 


[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)
[![arXiv](https://img.shields.io/badge/arXiv-2106.03598-b31b1b.svg)](https://arxiv.org/abs/2106.03598)
# A [Flaxformer](https://github.com/google/flaxformer) and [T5X](https://github.com/google-research/t5x) implementation for [SciFive](https://github.com/justinphan3110/SciFive) 



### BioT5X: Pretrained T5X Transformer for Biomedical Text Generation and Classification 


| Model           |    Size     | Step | Config  | Checkpoint  |
|:---------------:|:-----------:|:----:|:-------:|:-----------:|
| BioT5X    | base & large  | 1200000 | [T5_1_0 configs](https://github.com/justinphan3110/BioT5X/tree/main/configs/t5/t5_1_0)| `gs://scifive/biot5x/{size}/` |

### Set Up

#### Set up JAX with CUDA
```[python]
pip install jaxlib==0.4.1+cuda11.cudnn86 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```

#### Set up BioT5X
```
python3 setup.py
```


### Finetune Example

### Our example Fine-tunning notebook for the BLURB Tasks [finetunning_biot5x_blurb.ipynb](https://github.com/justinphan3110/SciFive/blob/main/biot5x/examples/finetunning_biot5x_blurb.ipynb)

```[python]
task2metric = {
  "ddi": "PRF1",
  "chemprot": "PRF1",
  "GAD": "PRF1",
  "BioASQ":"accuracy", "PubMedQA": "accuracy",
  "HoC":"hoc"
}

model_size = 'base'
task = 'HoC'
train_file = f'data/{task}/train_blurb.tsv'
test_file = f'data/{task}/test_blurb.tsv'

model_dir = f'out/{task}/{model_size}_{task}'
pretrained_path=f'biot5x_pubmed_pmc_{model_size}/{model_size}'

# See gin file for hyperparams like batch_size, input/target length, train steps, etc.
gin_file = f'configs/biot5x/finetune/base/{task}_blurb.gin'

metric = task2metric[task]

%run 'src/finetune_biot5x.py' \
  --gin_file="{gin_file}" \
  --gin.MODEL_DIR="'{model_dir}'" \
  --gin.INITIAL_CHECKPOINT_PATH="'{pretrained_path}'" \
  --task="{task}" \
  --metric="{metric}" \
  --train_file="{train_file}" \
  --predict_file="{test_file}"
```

## Results

### BLURB (Classification)
|           Task          | BioBERT<sub>base</sub> | PubmedBERT<sub>base</sub> | BioLinkBERT<sub>base</sub> | **BioT5X<sub>base</sub> (Ours)** |
|:-----------------------:|-----------------|-----------------|------------------|-----------------|
| <sub>**Named entity recognition**</sub>                                     
| BC5-chem                |      92.85      |      93.33      |       93.75      |    92.74         |
| BC5-disease             |      84.70      |      85.62      |       86.10      |    85.28         |
| NCBI-disease            |      89.13      |      87.82      |       88.18      |    89.05         |
| BC2GM                   |      83.82      |      84.52      |       84.90      |    83.2         |
| JNLPBA                  |      78.55      |      80.06      |       79.03      |    ****         |
| <sub>**Relation Extraction**</sub>                                     
| Chemprot                |      76.14      |      77.24      |       77.57      |    **77.40**    |
| GAD                     |      82.36      |      82.34      |       84.39      |    **83.66**    |
| DDI                     |      80.88      |      82.36      |       82.72      |    **82.63**    |
| <sub>**Document classification**</sub>
| HoC                     |      81.51      |      82.32      |       84.35      |    **82.39**    |
| <sub>**Question answering**</sub>
| BioASQ                  |      84.14      |      87.56      |       91.43      |    **91.43**    |
| PubMedQA                |      60.24      |      55.84      |       70.20      |    **67.60**    |



## Citations
If you use BioT5X model or our code for publications, please cite: 
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

