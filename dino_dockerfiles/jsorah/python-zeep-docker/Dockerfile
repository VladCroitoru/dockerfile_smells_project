FROM python:3.6
RUN apt-get update && \
    apt-get install -y \
    libxml2-dev libxmlsec1-dev libxmlsec1-openssl
RUN pip install zeep[xmlsec]