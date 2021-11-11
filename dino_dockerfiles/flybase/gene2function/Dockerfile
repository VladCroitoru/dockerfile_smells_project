FROM debian:jessie
MAINTAINER Josh Goodman <jogoodma@indiana.edu>

RUN apt-get update && apt-get install -y \
        curl \
        perl \
        perl-doc \
        libdancer2-perl \
        libjson-perl \
        libbio-perl-perl \
        cpanminus \
        make \
        gcc \
        gzip

RUN cpanm Search::Elasticsearch

RUN mkdir -p /g2f
RUN mkdir -p /data

COPY . /g2f/
COPY docker-entrypoint.sh /

VOLUME /g2f
VOLUME /data

EXPOSE 5000
ENTRYPOINT ["/docker-entrypoint.sh"]
