############################################################
# Dockerfile to build nginx container images
# Based on Alpine linux
# inspired by https://hub.docker.com/r/matriphe/alpine-nginx/
############################################################

# Use Alpine Linux
FROM tarzan79/alpine-base:latest

ENV TIMEZONE Europe/Paris

RUN	apk update && \
	apk upgrade && \
	apk add --update openssl nginx && \
	apk add --update tzdata && \
	cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
	echo "${TIMEZONE}" > /etc/timezone && \
	mkdir /etc/nginx/certificates && \
	openssl req \
		-x509 \
		-newkey rsa:2048 \
		-keyout /etc/nginx/certificates/key.pem \
		-out /etc/nginx/certificates/cert.pem \
		-days 365 \
		-nodes \
		-subj /CN=localhost && \
	mkdir /www && \
    chmod -R 777 /var/www && \
	apk del tzdata && \
	rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx

COPY /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# Expose ports
EXPOSE 80 443

# Add the files
ADD root /

CMD ["nginx"]
