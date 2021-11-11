# Tesseract OCR Runtime Environment - Docker Container
# with deu, ces and helpful aliases
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:alex-p/tesseract-ocr && \
    apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-deu tesseract-ocr-ces imagemagick && \
    apt-get remove -y software-properties-common && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/cache/* && \
    rm -rf /var/lib/log/* && \
    mkdir /home/work

COPY files/ /

WORKDIR /home/work
