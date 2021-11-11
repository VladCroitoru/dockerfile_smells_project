FROM eboraas/apache-php:jessie
MAINTAINER Thor Erik Lie <thor@thorerik.com>

ENV PBWP_VERSION="1.6"

RUN apt-get update && apt-get install -y php5-sqlite php5-curl wget

COPY ./docker-entrypoint.sh /

RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 80
CMD ["webpanel"]
