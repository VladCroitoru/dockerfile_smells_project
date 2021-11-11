FROM gcr.io/webera/base

COPY docker-entrypoint.sh /usr/local/bin/

RUN set -x && \
    apt-get update && apt-get install -qq -y git \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /git \
    && chown 1000:1000 /git \
    && chmod +rx /usr/local/bin/docker-entrypoint.sh 

USER 1000

VOLUME /git

WORKDIR /git

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
