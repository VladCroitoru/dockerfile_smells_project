FROM debian:latest
MAINTAINER Felix Barbeira <fbarbeira@gmail.com>

ENV CURATOR_VERSION 3

RUN apt-get update -qq && apt-get install -yqq wget
RUN wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb http://packages.elasticsearch.org/curator/${CURATOR_VERSION}/debian stable main" > /etc/apt/sources.list.d/curator.list
RUN apt-get update -qq && apt-get install -yqq python-elasticsearch-curator

ENTRYPOINT ["/usr/local/bin/curator"]
