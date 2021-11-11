# Docker image for Jenkins Enterprise by CloudBees master

FROM apemberton/jenkins-haproxy
MAINTAINER Nigel Harniman <nharniman@cloudbees.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
    groovy

EXPOSE 80 40001 40002 40003 40011 40012 40013

ADD /start-haproxy.sh /start-haproxy.sh
ADD /jocproxy.groovy /jocproxy.groovy
ADD /haproxy.cfg /etc/haproxy/haproxy.cfg
ADD /rsyslog-haproxy.conf /etc/rsyslog.d/haproxy.conf

ENTRYPOINT ["sh","/start-haproxy.sh"]



