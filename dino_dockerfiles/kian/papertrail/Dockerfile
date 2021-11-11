FROM quay.io/democracyworks/base:2015032400
MAINTAINER Democracy Works, Inc. <dev@turbovote.org>

RUN apt-get update && apt-get install -q -y rsyslog rsyslog-gnutls

ADD papertrail-bundle.pem /etc/papertrail-bundle.pem
ADD configure-and-run-rsyslog.sh /configure-and-run-rsyslog.sh
RUN echo "*.=notice;*.=warn |/dev/console" > /etc/rsyslog.d/50-default.conf

EXPOSE 514/udp

CMD ["/configure-and-run-rsyslog.sh"]
