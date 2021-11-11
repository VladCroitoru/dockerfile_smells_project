FROM node

MAINTAINER Rafael Roman "rafael@notastica.org"

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y python-dev tesseract-ocr tesseract-ocr-fra python-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && \
    pip install pytesseract Pillow
