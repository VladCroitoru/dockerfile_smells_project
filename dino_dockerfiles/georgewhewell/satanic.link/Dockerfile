FROM python:3.5-alpine

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY sataniclink sataniclink

CMD python sataniclink/app.py
