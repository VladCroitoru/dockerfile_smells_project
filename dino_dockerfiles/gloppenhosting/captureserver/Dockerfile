FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xfb40d3e6508ea4c8
RUN echo "deb http://deb.kamailio.org/kamailio jessie main" >> etc/apt/sources.list
RUN echo "deb-src http://deb.kamailio.org/kamailio jessie main" >> etc/apt/sources.list
RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -yqq kamailio rsyslog inotify-tools kamailio-outbound-modules kamailio-sctp-modules kamailio-tls-modules kamailio-websocket-modules kamailio-utils-modules kamailio-mysql-modules && rm -rf /var/lib/apt/lists/*

COPY kamailio.cfg /etc/kamailio/kamailio.cfg
COPY run.sh /run.sh
ENTRYPOINT [ "/run.sh" ]
