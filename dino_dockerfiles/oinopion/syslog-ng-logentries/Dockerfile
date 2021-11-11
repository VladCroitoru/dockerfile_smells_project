FROM debian:jessie
MAINTAINER Tomek Paczkowski <tomek@hauru.eu>
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y syslog-ng-core
COPY ./syslog-ng.conf /etc/syslog-ng/syslog-ng.conf
EXPOSE 514/udp
CMD ["/usr/sbin/syslog-ng", "--foreground", "--no-caps", "-f", "/etc/syslog-ng/syslog-ng.conf"]

