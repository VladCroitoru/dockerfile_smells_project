FROM python:3.9
ADD metadata_validation_conversion metadata_validation_conversion
WORKDIR metadata_validation_conversion
ADD requirements.txt ./
ADD run_daphne.sh ./
ADD run_celery.sh ./
ADD run_flower.sh ./
RUN pip install -r requirements.txt