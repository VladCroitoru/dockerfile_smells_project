FROM alpine:3.12
LABEL maintainer="Cyrille Nofficial<cynoffic@cyrilix.fr>"

ARG VERSION="v1.0.0"

ENV BASE_URL=False IMAGE_PROXY=False
ENV SECRET_KEY=""

RUN apk -U upgrade \
 && apk add -t build-dependencies \
    build-base \
    python3-dev \
    libffi-dev \
    libxslt-dev \
    libxml2-dev \
    openssl-dev \
    tar \
    ca-certificates \
 && apk add \
    su-exec \
    python3 \
    libxml2 \
    libxslt \
    openssl \
    tini \
 && apk add \
    uwsgi \
    uwsgi-python3 \
    uwsgi-http \
 && mkdir /usr/local/searx && cd /usr/local/searx \
 && wget -qO- https://github.com/asciimoo/searx/archive/${VERSION}.tar.gz | tar xz --strip 1 \
 && pip3 install --upgrade setuptools \
 && pip3 install --no-cache -r requirements.txt \
 && pip3 install Werkzeug==0.16.0 \
 && pip3 install -e . \
 && sed -i "s/127.0.0.1/0.0.0.0/g" searx/settings.yml \
 && apk del build-dependencies \
 && rm -f /var/cache/apk/*



COPY searx.ini /usr/local/searx/searx.ini
COPY run.sh /usr/local/bin/run.sh

RUN chmod 755 /usr/local/bin/run.sh


USER 1234
WORKDIR /usr/local/searx

EXPOSE 8888

ENTRYPOINT ["/usr/local/bin/run.sh"]
