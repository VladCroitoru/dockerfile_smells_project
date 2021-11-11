FROM python:2.7-slim

ENV OPENSSL_VERSION 1.0.1q

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
	make \
	libssl-dev \
	libffi-dev \
	gcc \
        git \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install lambda-uploader \
    && mkdir /data

RUN virtualenv /venv && . /venv/bin/activate \
    && mkdir -p /var/task && cd /var/task \
    && curl -O https://openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
    && tar xvf openssl-${OPENSSL_VERSION}.tar.gz \
    && mv openssl-${OPENSSL_VERSION} openssl-src \
    && cd openssl-src \
    && ./config no-shared no-ssl2 -fPIC --prefix=/var/task/openssl-${OPENSSL_VERSION} \
    && make depend && make && make install \
    && cd .. \
    && rm -rf openssl-src openssl*.tar.gz \
    && CFLAGS="-I/var/task/openssl-${OPENSSL_VERSION}/include" \
    LDFLAGS="-L/var/task/openssl-${OPENSSL_VERSION}/lib" \
    pip install --no-use-wheel cryptography \
    && cp -a /var/task/openssl-${OPENSSL_VERSION} /venv/lib/python2.7/site-packages/openssl-${OPENSSL_VERSION}

WORKDIR /data

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]
