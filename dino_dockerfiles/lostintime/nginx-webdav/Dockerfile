FROM nginx:1.12.2-alpine

LABEL maintainer="Lostintime <lostintime.dev@gmail.com>"

COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /data/www && \
	  mkdir -p /data/client_temp && \
		chown -R nginx:nginx /data

VOLUME [ "/data" ]
