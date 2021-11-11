FROM python:2.7.11-alpine

ENV DEBIAN_FRONTEND noninteractive
ENV ETCDCTL_VERSION v2.2.5
ENV DUMB_INIT_VERSION 1.0.1
ENV CONFD_VERSION 0.12.0-alpha3

# Native dependencies
RUN apk add --no-cache --update \
        pcre \
        bash \
        gettext \
        curl \
        openssl \
        libffi \
        openssh-client \

    # Etcdctl
    && curl -L https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz -o /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz \
    && cd /tmp && gzip -dc etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz | tar -xof -  \
    && cp -f /tmp/etcd-$ETCDCTL_VERSION-linux-amd64/etcdctl /usr/local/bin \

    # Confd
    && curl -L https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-${CONFD_VERSION}-linux-amd64 -o /usr/local/bin/confd \
    && chmod 555 /usr/local/bin/confd \

    # Dumb Init
    && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 \
    && chmod +x /usr/bin/dumb-init \

    # SSH Key for fleet
    && mkdir /root/.ssh  \
    && chmod  500 /root/.ssh  \
    && chown -R root:root /root/.ssh \

    # Cleanup
    && rm -rf /tmp/*

# Application dependencies
ADD requirements.txt /opt/cluster-deployer/requirements.txt
RUN apk add --no-cache --update --virtual build-dependencies \
      musl-dev \
      linux-headers \
      build-base \
      pcre-dev \
      libffi-dev \
      openssl-dev \

    # Python dependencies
    && pip install --ignore-installed  --no-cache-dir \
      supervisor==3.2.3 \
      supervisor-stdout  \
      -r /opt/cluster-deployer/requirements.txt \

    # Supervisor (Post Setup)
    && mkdir -p /var/log/supervisor \
    && ln -sf /etc/supervisor/supervisord.conf /etc/supervisord.conf \

    # Cleanup
    && apk del build-dependencies \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) -exec echo rm -rf '{}' + \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec echo rm -f '{}' +


# Custom Scripts
ADD bin/*.sh /usr/sbin/
RUN chmod +x /usr/sbin/*.sh

# Etc Config
ADD etc /etc

ADD . /opt/cluster-deployer

EXPOSE 9000

WORKDIR /opt/cluster-deployer

CMD ["/usr/bin/dumb-init", "/usr/sbin/supervisord-wrapper.sh"]
