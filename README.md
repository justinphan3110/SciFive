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


As described in our [paper](), we make public 6 version of SciFive, each one has been benchmarked to achieve state-of-the-art on different biomedical task. They are all available on our [Google Cloud bucket](https://console.cloud.google.com/storage/browser/scifive), we are working on release the models on HuggingFace also.

Instruction on access Cloud Storage from the command line with python library gsutil is described [here](https://cloud.google.com/storage/docs/gsutil)

### gsutil URI for 6 SciFive models:

* **SciFive Pubmed+PMC Base**: [gs://scifive/models/pubmed_pmc/base]() 
* **SciFive Pubmed+PMC Large**: [gs://scifive/models/pubmed_pmc/large]() 
* **SciFive Pubmed Base**: [gs://scifive/models/pubmed/base]() 
* **SciFive Pubmed+PMC Large**: [gs://scifive/models/pubmed/large]() 
* **SciFive PMC Large**: [gs://scifive/models/pmc/base]() 
* **SciFive PMC Large**: [gs://scifive/models/pmc/large]() 

### gsutil URI for Pretrain data:
* **Pubmed**: [gs://scifive/pretrain/pubmed]() 
* **PMC**: [gs://scifive/pretrain/pmc]() 


# HuggingFace
coming soon

## Datasets

All of the finetune dataset already pre-procossed into text-text format also availabe at [https://console.cloud.google.com/storage/browser/scifive/finetune]()

## Citations
If you use SciFive model or our code for publications, please cite: 
``` ```
