FROM python:2.7.11-alpine

ENV DEBIAN_FRONTEND noninteractive
ENV ETCDCTL_VERSION v2.2.5
ENV DUMB_INIT_VERSION 1.0.1

RUN apk add --no-cache --update \
        pcre \
        gettext \
        curl \
        openssl \

    # Etcdctl
    && curl -L https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz -o /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz \
    && cd /tmp && gzip -dc etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz | tar -xof -  \
    && cp -f /tmp/etcd-$ETCDCTL_VERSION-linux-amd64/etcdctl /usr/local/bin \

    # Dumb Init
    && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 \
    && chmod +x /usr/bin/dumb-init \

    # Cleanup
    && rm -rf /tmp/*

# Application dependencies
ADD requirements.txt /opt/cluster-orchestrator/requirements.txt
RUN apk add --no-cache --update --virtual build-dependencies \
      musl-dev \
      linux-headers \
      build-base \
      pcre-dev \
      libffi-dev \
      openssl-dev \

    # Python depdencies
    && pip install --ignore-installed  --no-cache-dir \
      supervisor==3.2.3 \
      supervisor-stdout  \
      -r /opt/cluster-orchestrator/requirements.txt \

    # Supervisor (Post Setup)
    && mkdir -p /var/log/supervisor \
    && ln -sf /etc/supervisor/supervisord.conf /etc/supervisord.conf \

    # Cleanup
    && apk del build-dependencies \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) -exec echo rm -rf '{}' + \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec echo rm -f '{}' +


# Supervisor Scripts
ADD bin/supervisord-wrapper.sh /usr/sbin/supervisord-wrapper.sh
RUN chmod +x /usr/sbin/supervisord-wrapper.sh

# Etc Config
ADD etc /etc

ADD . /opt/cluster-orchestrator

EXPOSE 9400

WORKDIR /opt/cluster-orchestrator

CMD ["/usr/bin/dumb-init", "/usr/sbin/supervisord-wrapper.sh"]
