FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -qqy keepalived && rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
COPY keepalived.conf /etc/keepalived/keepalived.conf

ENTRYPOINT [ "/run.sh" ]
