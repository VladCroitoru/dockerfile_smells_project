FROM python

WORKDIR /api

COPY data/test_predictions.csv .

COPY least_bad_model.mdl .

COPY preprocessing.py .

COPY claim_classifier.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY api.py .

CMD ["python3", "./api.py"]
