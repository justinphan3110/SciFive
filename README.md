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


SciFive provided a Text-Text framework for biomedical language and natural language in NLP. Under the [T5](https://github.com/google-research/text-to-text-transfer-transformer)'s framework and desrbibed in the paper [SciFive: a text-to-text transformer model for biomedical literature](), SciFive achieve state-of-the-art and competitive results on multiple biomedical-natural language tasks. 

# Google Cloud Storage 

Our base Google Cloud Storage URI is at [gs://scifive]()


As described in our [paper](https://arxiv.org/abs/2106.03598), we make public 6 version of SciFive, each one has been benchmarked to achieve state-of-the-art on different biomedical task. They are all available on our [Google Cloud bucket](https://console.cloud.google.com/storage/browser/scifive), we are working on release the models on HuggingFace also.

Instruction on access Cloud Storage from the command line with python library gsutil is described [here](https://cloud.google.com/storage/docs/gsutil)

### gsutil URI for 6 SciFive models:

* **SciFive Pubmed+PMC Base**: [gs://scifive/models/pubmed_pmc/base]() 
* **SciFive Pubmed+PMC Large**: [gs://scifive/models/pubmed_pmc/large]() 
* **SciFive Pubmed Base**: [gs://scifive/models/pubmed/base]() 
* **SciFive Pubmed Large**: [gs://scifive/models/pubmed/large]() 
* **SciFive PMC Base**: [gs://scifive/models/pmc/base]() 
* **SciFive PMC Large**: [gs://scifive/models/pmc/large]() 

### gsutil URI for Pretrain data:
* **Pubmed**: [gs://scifive/pretrain/pubmed]() 
* **PMC**: [gs://scifive/pretrain/pmc]() 


### Example
Coming Soon


# HuggingFace
* **SciFive Pubmed+PMC**: [Base](https://huggingface.co/razent/SciFive-base-Pubmed_PMC) | [Large](https://huggingface.co/razent/SciFive-large-Pubmed_PMC) 
* **SciFive Pubmed**: [Base](https://huggingface.co/razent/SciFive-base) | [Large](https://huggingface.co/razent/SciFive-lage-Pubmed) 
* **SciFive PMC**: [Base](https://huggingface.co/razent/SciFive-base-PMC) | [Large](https://huggingface.co/razent/SciFive-large-PMC)

## Datasets

All of the finetune dataset already pre-procossed into text-text format also availabe at [this](https://console.cloud.google.com/storage/browser/scifive/finetune)

## 📊&nbsp; Expected Results 

<a name="function-documentation-generation"></a>
 * <b>💻&nbsp; Function Documentation Generation (Bleu):</b><br/>
 
<!-- |   Language / Model   |     Python     |      Java      |       Go       |      Php       |      Ruby      |   JavaScript   |
| -------------------- | :------------: | :------------: | :------------: | :------------: | :------------: | :------------: |
|   CodeTrans-ST-Small    |      17.31     |     16.65      |     16.89      |     23.05      |      9.19      |      13.7      |
|   CodeTrans-ST-Base     |      16.86     |     17.17      |     17.16      |     22.98      |      8.23      |      13.17     |   
|   CodeTrans-TF-Small    |      19.93     |     19.48      |     18.88      |     25.35      |     13.15      |      17.23     |
|   CodeTrans-TF-Base     |      20.26     |     20.19      |     19.50      |     25.84      |     14.07      |      18.25     |
|   CodeTrans-TF-Large    |      20.35     |     20.06      |   **19.54**    |     26.18      |     14.94      |    **18.98**   |
|   CodeTrans-MT-Small    |      19.64     |     19.00      |     19.15      |     24.68      |     14.91      |      15.26     |
|   CodeTrans-MT-Base     |    **20.39**   |     21.22      |     19.43      |   **26.23**    |   **15.26**    |      16.11     |
|   CodeTrans-MT-Large    |      20.18     |   **21.87**    |     19.38      |     26.08      |     15.00      |      16.23     |
|   CodeTrans-MT-TF-Small |      19.77     |     20.04      |     19.36      |     25.55      |     13.70      |      17.24     |
|   CodeTrans-MT-TF-Base  |      19.77     |     21.12      |     18.86      |     25.79      |     14.24      |      18.62     |
|   CodeTrans-MT-TF-Large |      18.94     |     21.42      |     18.77      |     26.20      |     14.19      |      18.83     |
|   State of the art   |      19.06     |     17.65      |     18.07      |     25.16      |     12.16      |      14.90     |
 
<a name="source-code-summarization"></a>
 * <b>💻&nbsp; Source Code Summarization (Bleu):</b><br/>
 
|   Language / Model   |     Python     |       SQL      |       C#       |
| -------------------- | :------------: | :------------: | :------------: |
|   CodeTrans-ST-Small    |      8.45      |     17.55      |     19.74      |
|   CodeTrans-ST-Base     |      9.12      |     15.00      |     18.65      | 
|   CodeTrans-TF-Small    |     10.06      |     17.71      |     20.40      |
|   CodeTrans-TF-Base     |     10.94      |     17.66      |     21.12      |
|   CodeTrans-TF-Large    |     12.41      |     18.40      |     21.43      |
|   CodeTrans-MT-Small    |     13.11      |     19.15      |     22.39      |
|   CodeTrans-MT-Base     |   **13.37**    |     19.24      |     23.20      |
|   CodeTrans-MT-Large    |     13.24      |     19.40      |   **23.57**    |
|   CodeTrans-MT-TF-Small |     12.10      |     18.25      |     22.03      |
|   CodeTrans-MT-TF-Base  |     10.64      |     16.91      |     21.40      |
|   CodeTrans-MT-TF-Large |     12.14      |   **19.98**    |     21.10      |
|   State of the art   |       --       |     18.40      |     20.50      |

<a name="code-comment-generation"></a>
 * <b>💻&nbsp; Code Comment Generation (Bleu):</b><br/>
 
|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     37.98      |
|   CodeTrans-ST-Base     |     38.07      |
|   CodeTrans-TF-Small    |     38.56      |
|   CodeTrans-TF-Base     |     39.06      |
|   CodeTrans-TF-Large    |   **39.50**    |
|   CodeTrans-MT-Small    |     20.15      |
|   CodeTrans-MT-Base     |     27.44      |
|   CodeTrans-MT-Large    |     34.69      |
|   CodeTrans-MT-TF-Small |     38.37      |
|   CodeTrans-MT-TF-Base  |     38.90      |
|   CodeTrans-MT-TF-Large |     39.25      |
|   State of the art   |     38.17      |

<a name="commit-message-generation"></a>
 * <b>💻&nbsp; Commit Message Generation (Bleu):</b><br/>
 
|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     39.61      |
|   CodeTrans-ST-Base     |     38.67      |
|   CodeTrans-TF-Small    |     44.22      |
|   CodeTrans-TF-Base     |     44.17      |
|   CodeTrans-TF-Large    |   **44.41**    |
|   CodeTrans-MT-Small    |     36.17      |
|   CodeTrans-MT-Base     |     39.25      |
|   CodeTrans-MT-Large    |     41.18      |
|   CodeTrans-MT-TF-Small |     43.96      |
|   CodeTrans-MT-TF-Base  |     44.19      |
|   CodeTrans-MT-TF-Large |     44.34      |
|   State of the art   |     32.81      |

<a name="api-sequence-recommendation"></a>
 * <b>💻&nbsp; API Sequence Recommendation (Bleu):</b><br/>
 
|   Language / Model   |      Java      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     68.71      |
|   CodeTrans-ST-Base     |     70.45      |
|   CodeTrans-TF-Small    |     68.90      |
|   CodeTrans-TF-Base     |     72.11      |
|   CodeTrans-TF-Large    |     73.26      |
|   CodeTrans-MT-Small    |     58.43      |
|   CodeTrans-MT-Base     |     67.97      |
|   CodeTrans-MT-Large    |     72.29      |
|   CodeTrans-MT-TF-Small |     69.29      |
|   CodeTrans-MT-TF-Base  |     72.89      |
|   CodeTrans-MT-TF-Large |   **73.39**    |
|   State of the art   |     54.42      |

<a name="programming-language-and-synthesis"></a>
 * <b>💻&nbsp; Programming Language and Synthesis (Accuracy):</b><br/>
 
|   Language / Model   |      LISP      |
| -------------------- | :------------: |
|   CodeTrans-ST-Small    |     89.43      |
|   CodeTrans-ST-Base     |     89.65      |
|   CodeTrans-TF-Small    |     90.30      |
|   CodeTrans-TF-Base     |     90.24      |
|   CodeTrans-TF-Large    |     90.21      |
|   CodeTrans-MT-Small    |     82.88      |
|   CodeTrans-MT-Base     |     86.99      |
|   CodeTrans-MT-Large    |     90.27      |
|   CodeTrans-MT-TF-Small |   **90.31**    |
|   CodeTrans-MT-TF-Base  |     90.30      |
|   CodeTrans-MT-TF-Large |     90.17      |
|   State of the art   |     85.80      | -->

## 🤵&nbsp; Team

 * <b>The National Institutes of Health:</b><br/>

| James Anibal       |       Long Phan  |  Alec Peltekian | Erol Bahadiroglu |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
| <img width=120/ src="https://faes.org/sites/default/files/james_anibal.png"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4E03AQFqMmKjyQRtAQ/profile-displayphoto-shrink_400_400/0/1594192915473?e=1628726400&v=beta&t=9rPFc2GnImXXDtPoXxoS0432LjybyWJVL0b_fn6aLew"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4E03AQGIjDegQmApcQ/profile-displayphoto-shrink_200_200/0/1573082873285?e=1628121600&v=beta&t=kuXiDY3qIzmAAqDvZugOgCAcFlaGEw4fRbJf1pAdMPY"> | <img width=120/ src="https://media-exp1.licdn.com/dms/image/C4D03AQGygdk5u9F1HA/profile-displayphoto-shrink_200_200/0/1522727407036?e=1628121600&v=beta&t=Z_4O17wxhWnatS7Vye0VekyIJiKBMOvpdyCyO3pIaVY"> |

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
