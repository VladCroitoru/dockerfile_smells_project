FROM soriyath/alpine-supervisor
MAINTAINER Sumi Straessle

RUN apk update \
	&& apk upgrade \
	&& apk add rsyslog
ADD ./rsyslog.conf /etc/rsyslog.conf
ADD ./rsyslog.sv.conf /etc/supervisor/conf.d/rsyslog.sv.conf

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
