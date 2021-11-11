FROM ubuntu:16.04

USER root

COPY entrypoint.sh /
COPY script /root/script
COPY csv /root/csv

RUN apt-get update && apt-get install -y --no-install-recommends \
    python \
    python-dev \
    python-pip \
    python-setuptools \
    bash \
    curl \
    vim \
 && pip install --upgrade pip==9.0.1 \
 && pip install es2csv \
 && pip install numpy \
 && pip install pandas \
 && chmod +x entrypoint.sh /root/script/* \
 && chmod a+r /root/script/config

ENTRYPOINT ["/entrypoint.sh"]
