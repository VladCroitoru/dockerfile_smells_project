FROM python:2.7.15-alpine3.8

MAINTAINER ncoussem

ENV SABNZBD_VERSION=2.3.9
ENV PAR2CMDLINE_VERSION=v0.8.0


RUN apk upgrade --update \
    && apk add git make automake autoconf g++ openssl unrar ca-certificates p7zip libffi-dev openssl-dev \
    && pip install --upgrade --no-cache-dir pip cheetah pyopenssl sabyenc\
    && git clone --depth 1 --branch ${PAR2CMDLINE_VERSION} https://github.com/Parchive/par2cmdline.git \
    && cd /par2cmdline \
    && aclocal \
    && automake --add-missing \
    && autoconf \
    && ./configure \
    && make \
    && make install \
    && rm -rf /par2cmdline \
    && cd / \
    && apk add mercurial \
    && hg clone https://bitbucket.org/dual75/yenc\
    && cd /yenc \
    && python setup.py build \
    && python setup.py install \
    && apk del mercurial \
    && cd / \
    && rm -rf /yenc \
    && git clone --depth 1 --branch ${SABNZBD_VERSION} https://github.com/sabnzbd/sabnzbd.git  \
    && apk del git gcc g++ make automake autoconf libffi-dev musl-dev \
    && rm -rf /var/cache/apk/ /sabnzbd/.git /tmp/*


EXPOSE 8080 9090

VOLUME ["/config", "/data"]

WORKDIR /sabnzbd

CMD su -pc "python ./SABnzbd.py -b 0 -f /config/ -s 0.0.0.0:8080"


