FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xfb40d3e6508ea4c8
RUN echo "deb http://deb.kamailio.org/kamailio jessie main" >> etc/apt/sources.list
RUN echo "deb-src http://deb.kamailio.org/kamailio jessie main" >> etc/apt/sources.list
RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -qqy \
  kamailio \
  rsyslog \
  inotify-tools \
  kamailio-outbound-modules \
  kamailio-sctp-modules \
  kamailio-tls-modules \
  kamailio-websocket-modules \
  kamailio-utils-modules \
  kamailio-mysql-modules \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN echo "local0.*                        -/var/log/kamailio.log" >> /etc/rsyslog.conf

COPY run.sh /run.sh
COPY dispatcher_watch.sh /
COPY kamailio.cfg /etc/kamailio/kamailio.cfg
COPY dispatcher.list /etc/kamailio/dispatcher.list

CMD /run.sh
