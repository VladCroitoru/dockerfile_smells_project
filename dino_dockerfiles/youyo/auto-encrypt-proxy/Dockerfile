FROM youyo/ngx-mruby:1.20.2
ENV REDIS_HOST 127.0.0.1
ENV REDIS_PORT 6379
ENV TTL 5184000
RUN apk add --no-cache --update openssl && \
	openssl dhparam 2048 -out /etc/nginx/dhparams.pem
ADD ssl /etc/nginx/ssl
ADD conf/nginx.conf /etc/nginx/conf/nginx.conf
ADD hook /usr/share/nginx/hook
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
