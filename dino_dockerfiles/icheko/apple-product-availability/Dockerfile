FROM php:5-alpine
MAINTAINER "Jose Pacheco" <jose@icheko.com>
COPY app /app
WORKDIR /app

RUN apk add --update postfix supervisor; \
	echo $'\n# Silence the EAI warning on alpine linux\nsmtputf8_enable = no' >> /etc/postfix/main.cf

COPY	docker-config/supervisord.conf /etc/supervisord.conf

CMD /usr/bin/supervisord -c /etc/supervisord.conf