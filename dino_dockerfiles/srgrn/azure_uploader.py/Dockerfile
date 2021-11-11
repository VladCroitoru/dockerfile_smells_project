FROM python:alpine

MAINTAINER Eran Zimbler <eran@zimbler.net>

WORKDIR /src
ADD azure_uploader.py /src/
ADD requirements.txt /src/


RUN apk add --update --no-cache gcc g++ make libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python","azure_uploader.py"]