FROM alpine:edge
MAINTAINER Vincent Rouille <vincent@speedy37.fr>

RUN apk add --no-cache duplicity lftp librsync \
 && apk add --no-cache py-boto py-paramiko py2-pip py-cryptography ca-certificates \
 && apk add --no-cache py-cffi \
 && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing py-netifaces  \
 && pip install pyrax b2 dropbox && rm -r /root/.cache
COPY b2backend.py /usr/lib/python2.7/site-packages/duplicity/backends/b2backend.py
RUN  python -m compileall /usr/lib/python2.7/site-packages/duplicity/backends/b2backend.py
VOLUME /root/.cache/duplicity /tmp

CMD ["duplicity", "--help"]
