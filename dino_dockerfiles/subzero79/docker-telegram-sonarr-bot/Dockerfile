FROM mhart/alpine-node:latest
MAINTAINER subzero79

ADD src/ /root/

RUN apk add --update unzip wget supervisor nano 

RUN mv /root/supervisord.conf /etc/supervisord.conf && \
	mkdir /app /config && \
	wget --no-check-certificate https://github.com/onedr0p/telegram-sonarr-bot/archive/master.zip -P /app && \
	unzip /app/master.zip -d /app && \
	rm /app/master.zip

RUN cd /app/telegram-sonarr-bot-master && npm install

RUN apk del unzip wget

VOLUME /config

CMD ["/bin/ash","/root/startup.sh"]
