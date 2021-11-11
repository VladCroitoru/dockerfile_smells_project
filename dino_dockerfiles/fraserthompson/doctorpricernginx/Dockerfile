FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY usrlocalbin /usr/local/bin

RUN apk add --update --no-cache openssl certbot && \
    chmod +x /docker-entrypoint.sh && \
    chmod +x /usr/local/bin/certbot-get && \
    chmod +x /usr/local/bin/certbot-renew

RUN set -x \
    && deluser xfs \
    && addgroup -g 33 -S www-data \
	&& addgroup -g 1000 -S varwwwusers \
	&& adduser -u 33 -D -S -G varwwwusers www-data

ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]

VOLUME ["/socks"]