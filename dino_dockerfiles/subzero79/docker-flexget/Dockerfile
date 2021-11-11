FROM frolvlad/alpine-python2:latest
MAINTAINER subzero79

ENV DAEMON_USERNAME="flexget" DAEMON_NAME="Flexget" TERM=xterm 


ADD src/ /root/

RUN apk add --update gcc supervisor nano ca-certificates python-dev musl-dev && \
	cp /root/supervisord.conf /etc/ && \
	adduser ${DAEMON_USERNAME} -D

RUN pip install --upgrade pip && pip install flexget


RUN rm -rf /root/.cache

VOLUME /config

EXPOSE 5050

CMD ["/bin/ash","/root/startup.sh"]

