# SciFive

SciFive provided a Text-Text framework for biomedical language and natural language in NLP. Under the [T5](https://github.com/google-research/text-to-text-transfer-transformer)'s framework and desrbibed in the paper [SciFive: a text-to-text transformer modelfor biomedical literature](), SciFive achieve state-of-the-art and competitive results on multiple biomedical-natural language tasks. 

# Google Cloud Storage 

As described in our [paper](), we make public 6 version of SciFive, each one has been benchmarked to achieve state-of-the-art on different biomedical task. They are all available on our [Google Cloud bucket](https://console.cloud.google.com/storage/browser/scifive), we are working on release the models on HuggingFace also.

Instruction on access Cloud Storage from the command line with python library gsutil is described [here](https://cloud.google.com/storage/docs/gsutil)

### gsutil URI for 8 SciFive models:

* **SciFive Pubmed+PMC Base**: [gs://scifive/pubmed_pmc/base]() 
* **SciFive Pubmed+PMC Large**: [gs://scifive/pubmed_pmc/large]() 
* **SciFive Pubmed Base**: [gs://scifive/pubmed/base]() 
* **SciFive Pubmed+PMC Large**: [gs://scifive/pubmed/large]() 
* **SciFive PMC Large**: [gs://scifive/pmc/base]() 
* **SciFive PMC Large**: [gs://scifive/pmc/large]() 


# HuggingFace
coming soon

## Datasets

All of the pretraining dataset and fine-tune dataset already pre-procossed into text-text format also availabe at [https://console.cloud.google.com/storage/browser/scifive]()
