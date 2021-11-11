FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -yqq php5-cli php5-mysql gcc xinetd rsyslog && rm -rf /var/lib/apt/lists/*

RUN echo "agi             4573/tcp                        # FAST AGI entry" >> /etc/services

RUN mkdir /agi
COPY agiLaunch.sh /
COPY agi.php /agi/
COPY xinetd_agi /etc/xinetd.d/agi

EXPOSE 4573

CMD service rsyslog start && xinetd -stayalive -dontfork -pidfile /var/run/xinetd.pid
