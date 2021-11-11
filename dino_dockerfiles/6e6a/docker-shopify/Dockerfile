FROM debian:jessie

RUN apt-get update && apt-get install -y \
    curl python \
    && curl -s https://raw.githubusercontent.com/Shopify/themekit/master/scripts/install | python

ENV LC_ALL=C.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
    
WORKDIR /srv
VOLUME /srv

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
