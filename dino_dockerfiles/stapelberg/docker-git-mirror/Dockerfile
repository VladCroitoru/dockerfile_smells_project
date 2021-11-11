FROM debian:jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ADD git-mirror.sh /git-mirror.sh

USER nobody

VOLUME /git

ENTRYPOINT ["/git-mirror.sh"]
