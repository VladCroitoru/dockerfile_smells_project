FROM python:3.8.6-buster

COPY api /api
COPY StopFAIke /StopFAIke
COPY models/StopFAIke/bert_en_uncased_L-12_H-768_A-12 /models/StopFAIke/bert_en_uncased_L-12_H-768_A-12
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
