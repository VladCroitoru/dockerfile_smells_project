FROM ubuntu:zesty

RUN apt-get update && apt-get install -y \
        curl \
        gcc \
        git \
        make \
        python \
        python-pip \
        unzip \
    && apt-get clean

WORKDIR /root

RUN git clone https://github.com/stanfordnlp/GloVe --branch 1.2 --single-branch \
    && cd GloVe \
    && make \
    && pip install \
        numpy

RUN apt-get clean \
    && rm -rf /var/tmp /tmp /var/lib/apt/lists/*

VOLUME /data