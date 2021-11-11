FROM alpine:3.5

# Install some needed packages
RUN apk add --update ca-certificates python python-dev py-pip build-base libffi-dev openssl openssl-dev bash

#Python requirements
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN python -m textblob.download_corpora