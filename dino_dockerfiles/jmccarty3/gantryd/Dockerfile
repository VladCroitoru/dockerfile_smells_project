FROM gliderlabs/alpine


RUN apk --update upgrade && apk add python py-pip ca-certificates openssl haproxy fuse && \
    rm -rf /var/cache/apk/* && \
    wget https://github.com/jmccarty3/gantryd/archive/master.zip && \
    unzip master.zip && mv gantryd-master gantryd

RUN apk --update add --virtual build-deps python-dev build-base linux-headers && \
    pip install docker-py termcolor 'psutil >=2.2.1,<3.0' jinja2 python-etcd peewee watchdog && \
    apk del build-deps && \
    rm -rf /var/cache/apk/*

ADD . /gantryd
WORKDIR /gantryd
