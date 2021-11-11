FROM ywx217/docker-webmanage-base:latest
MAINTAINER Wenxuan Yang "ywx217@gmail.com"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
        python2.7 \
        python-dev \
        python-gevent \
        python-pip \
		build-essential net-tools uuid-dev \
        libzmq3 libzmq3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    redis \
    pymongo==2.8 \
    pyzmq \
    msgpack-python

WORKDIR /python
COPY ./*.py /python/
COPY ./*.sh /python/
COPY ./_queue_data.base64 /python/
COPY ./zeroactor /python/zeroactor
RUN chmod +x /python/run.sh
