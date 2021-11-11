FROM python:3.6.2-alpine

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY elsa.py /elsa.py

CMD python /elsa.py
