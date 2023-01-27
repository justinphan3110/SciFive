exit 0;

export model_size=base

### Configure Pretrained Path here
### Example download BioT5X base model
### mkdir biot5x_base
### gsutil -m cp -r gs://scifive/biot5x/base/* biot5x_base/
export pretrained_path=../../biot5x_$model_size

############################### NER: BC5CDR_chem ###############################
task=BC5CDR_chem
train_file=../data/$task/train_blurb.tsv
test_file=../data/$task/test_blurb.tsv
dev_file=../data/$task/dev_blurb.tsv
gin_file=../configs/biot5x/finetune/base/BC5CDR_chem_blurb.gin
metric=ner_metric
model_dir = out/$task/$model_size


python3 -u ../src/finetune_biot5x.py \
  --gin_file=$gin_file \
  --gin.MODEL_DIR=$model_dir \
  --gin.INITIAL_CHECKPOINT_PATH=$pretrained_path \
  --task=$task \
  --metric=$metric \
  --train_file=$train_file \
  --predict_file=$test_file

############################### NER: NCBI_disease ###############################
task=NCBI_disease
train_file=../data/$task/train_blurb.tsv
test_file=../data/$task/test_blurb.tsv
dev_file=../data/$task/dev_blurb.tsv
gin_file=../configs/biot5x/finetune/base/NCBI_disease_blurb.gin
metric=ner_metric
model_dir = out/$task/$model_size

python3 -u ../src/finetune_biot5x.py \
  --gin_file=$gin_file \
  --gin.MODEL_DIR=$model_dir \
  --gin.INITIAL_CHECKPOINT_PATH=$pretrained_path \
  --task=$task \
  --metric=$metric \
  --train_file=$train_file \
  --predict_file=$test_file