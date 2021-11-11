FROM python:3.5.1-alpine

ENV ETCDCTL_VERSION v2.2.5
ENV DUMB_INIT_VERSION 1.0.1
ENV CONFD_VERSION 0.12.0-alpha3

# Native dependencies
RUN \
    apk add --no-cache --update --virtual build-dependencies \
      wget \
      openssl \

    # Etcdctl
    && wget --no-check-certificate -O /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz \
    && cd /tmp && gzip -dc etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz | tar -xof -  \
    && cp -f /tmp/etcd-$ETCDCTL_VERSION-linux-amd64/etcdctl /usr/local/bin \

    # Dumb Init
    && wget --no-check-certificate  -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 \
    && chmod +x /usr/bin/dumb-init \

    # Cleanup
    && apk del build-dependencies \
    && rm -rf ~/.cache /tmp/*

# Application dependencies
ADD requirements.txt /opt/mongo-connector/requirements.txt
RUN \
    # Python dependencies
    pip3 install --ignore-installed  --no-cache-dir \
      -r /opt/mongo-connector/requirements.txt \

    # Cleanup
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) -exec echo rm -rf '{}' + \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec echo rm -f '{}' + \
    && rm -rf /usr/src/python ~/.cache /tmp/*


ADD . /opt/mongo-connector/
RUN chmod +x /opt/mongo-connector/run.sh

WORKDIR /opt/mongo-connector

CMD ["/usr/bin/dumb-init", "/opt/mongo-connector/run.sh"]
