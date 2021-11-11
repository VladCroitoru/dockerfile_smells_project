FROM alpine:latest
MAINTAINER Kyle Ondy <kyle@ondy.me>

ENV LEXICON_VERSION 2.1.10
ENV DEHYDRATED_VERSION 0.5.0

run apk add --update \
        bash \
        curl \
        git \
        openssl \
        py-pip \
        python && \

    # Dehydrated
    git clone https://github.com/lukas2511/dehydrated.git /srv/dehydrated && \
    cd /srv/dehydrated && git checkout tags/v${DEHYDRATED_VERSION} && \

    # Lexicon
    git clone https://github.com/AnalogJ/lexicon.git /srv/lexicon && \
    cd /srv/lexicon && git checkout tags/v${LEXICON_VERSION} && \
    pip install /srv/lexicon[route53] && \
    cp /srv/lexicon/examples/dehydrated.default.sh /srv/dehydrated/ && \
    chmod +x /srv/dehydrated/dehydrated.default.sh


ADD dns-certbot.sh /dns-certbot.sh
RUN chmod +x /dns-certbot.sh

ENTRYPOINT  [ "/dns-certbot.sh" ]
