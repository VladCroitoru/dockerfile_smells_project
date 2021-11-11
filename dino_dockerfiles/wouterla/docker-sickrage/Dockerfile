FROM alpine:edge
MAINTAINER tim@haak.co

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US.UTF-8' \
    TERM='xterm'

RUN apk -U upgrade && \
    apk -U add \
        ca-certificates \
        gcc git g++ \
        linux-headers libxml2 libxml2-dev libffi-dev libxslt-dev \
        py2-pip python python-dev py-libxml2 py2-libxslt py-lxml \
        make mercurial \
        nodejs \
        openssl-dev \
        tzdata \
        unrar \
        && \
    pip install --upgrade pip && \
    pip --no-cache-dir install --upgrade setuptools && \
    pip --no-cache-dir install --upgrade pyopenssl cheetah requirements && \
    git clone --depth 1 https://github.com/SickChill/SickChill.git /SickChill && \
#    pip install --user -U -r /SickChill/requirements/requirements.txt  && \
    apk del make gcc g++ python-dev && \
    rm -rf /tmp && \
    rm -rf /var/cache/apk/*

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

VOLUME ["/config", "/data", "/cache", "/scripts"]

EXPOSE 8081

CMD ["/start.sh"]
