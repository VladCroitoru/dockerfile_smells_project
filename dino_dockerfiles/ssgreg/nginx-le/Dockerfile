FROM nginx:alpine

ADD ./etc/nginx/nginx.conf /etc/nginx/nginx.conf
ADD entrypoint.sh /entrypoint.sh

RUN \
  apk add --update certbot openssl coreutils && \
  rm /etc/nginx/conf.d/default.conf && \
  rm -rf /var/cache/apk/*

CMD ["/entrypoint.sh"]

