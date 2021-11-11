FROM debian:unstable
MAINTAINER Philipp A. Baer <github@ph.baer.one>

ENV JHOVE_PATH=/opt/jhove/
ENV CLASSPATH=$JHOVE_CONF/bin

RUN apt-get update && \
    apt-get install -y scantailor tesseract-ocr tesseract-ocr-eng \
    tesseract-ocr-deu tesseract-ocr-deu-frak tesseract-ocr-equ \
    tesseract-ocr-fra tesseract-ocr-ita tesseract-ocr-nld \
    sane-utils pdftk curl default-jre && \
    curl -L -o jhove.tar.gz "https://sourceforge.net/projects/jhove/files/jhove/JHOVE%201.11/jhove-1_11.tar.gz/download" && \
    tar xfz jhove.tar.gz && \
    mkdir -p /var/scan && \
    mkdir -p /opt && \
    mkdir -p /root/jove/conf && \
    mv jhove /opt

COPY scan.sh /usr/local/bin/
COPY jhove.conf /root/jhove/conf/

RUN chmod +x /usr/local/bin/scan.sh

VOLUME /var/scan

