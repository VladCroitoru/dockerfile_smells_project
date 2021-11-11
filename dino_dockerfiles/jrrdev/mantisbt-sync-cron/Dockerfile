FROM webwurst/go-cron

MAINTAINER jrrdev

ENV LOCAL_TIME_ZONE "Europe/Paris"

WORKDIR /mantis-sync-cron/

COPY ./scripts/tasks.sh ./

RUN chmod +x ./tasks.sh && \
	sync && \
	echo "http://dl-cdn.alpinelinux.org/alpine/v`cat /etc/alpine-release | cut -c -3`/main" > /etc/apk/repositories && \
	echo "http://dl-cdn.alpinelinux.org/alpine/v`cat /etc/alpine-release | cut -c -3`/community" >> /etc/apk/repositories && \
	apk add -U tzdata && \
	rm -rf /var/cache/apk/* && \
	cp /usr/share/zoneinfo/$LOCAL_TIME_ZONE /etc/localtime

EXPOSE 18080
