FROM python:latest

WORKDIR /ocps-covid
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY templates/ templates/
COPY *.py ./