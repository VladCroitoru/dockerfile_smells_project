FROM alpine:3.4

MAINTAINER Luca Agostini <agostini.luca@gmail.com>

RUN apk add --update \
        bash \
        g++ \
        python \
        python-dev \
        py-pip \
        py-setuptools && \
    rm -rf /var/cache/apk/* && \
    pip install --no-cache-dir --upgrade --force-reinstall \
        pip \
        pyzmq \
        locustio

COPY files/etc/docker/start.sh /etc/docker/start.sh
RUN chmod +x /etc/docker/start.sh

CMD ["/etc/docker/start.sh"]
