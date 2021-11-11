FROM phusion/baseimage:0.9.22

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git \
        bzip2 \
        net-tools \
        curl \
        nano \
        build-essential \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        libpq-dev \
        python-libxml2 \
        libxslt1-dev \
        poppler-utils \
        sudo \
        wget \
        unzip && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -y && \
    rm -rf /root/.cache/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade gunicorn==19.6.0 gevent==1.1.2 supervisor==3.3.0 futures==3.0.5 psycogreen==1.0 psycopg2==2.6.1 json-logging-py==0.2

ADD base /base
