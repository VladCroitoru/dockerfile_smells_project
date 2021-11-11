FROM alpine:latest
MAINTAINER Sumi Straessle

ENV PYTHON_VERSION=2.7.12-r0
ENV PY_PIP_VERSION=8.1.2-r0
ENV SUPERVISOR_VERSION=3.3.0

RUN apk update \
	&& apk upgrade \
	&& apk add -u python=$PYTHON_VERSION py-pip=$PY_PIP_VERSION
RUN pip install supervisor==$SUPERVISOR_VERSION \
	&& mkdir -p /etc/supervisor/conf.d
ADD supervisor.conf /etc/supervisor/supervisor.conf

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
