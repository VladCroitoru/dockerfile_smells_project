FROM alpine:latest

RUN apk --no-cache --update add bind
RUN mkdir -p /var/cache/bind /var/log/named \
	&& touch /var/log/named/named.log \
	&& chmod 777 /var/log/named/named.log

EXPOSE 53

CMD ["named", "-c", "/etc/bind/named.conf", "-g", "-u", "named"]