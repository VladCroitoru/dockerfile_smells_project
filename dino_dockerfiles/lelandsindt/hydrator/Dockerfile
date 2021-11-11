FROM alpine
RUN apk --update upgrade && \
    apk add --no-cache \
      nginx \
      openssl \
      runit \
      curl \
      bash && \
      rm -rf /var/cache/apk/*
ADD https://raw.githubusercontent.com/lukas2511/dehydrated/v0.6.2/dehydrated           /usr/bin/dehydrated
ADD https://raw.githubusercontent.com/lukas2511/dehydrated/v0.6.2/docs/examples/config /etc/dehydrated/config
ADD usr/bin/* /usr/bin/
ADD etc/service/ /etc/service/ 
ADD etc/nginx-80/* /etc/nginx-80/
ADD etc/nginx/conf.d/* /etc/nginx/conf.d/
ADD var/www/hydrated/* /var/www/hydrated/
RUN chmod 700 -v /usr/bin/dehydrated /usr/bin/hydrator /usr/bin/hook.sh /usr/bin/start_runit && \
    chmod 700 -Rv /etc/service && \
    mkdir -p /var/www/dehydrated/ && \
    mkdir -p /run/nginx/ && \
    touch /var/www/dehydrated/nginx && \
    chown 0:0 -Rv /usr/bin/dehydrated /usr/bin/hydrator /var/www/dehydrated /etc/nginx-80 /etc/nginx /etc/dehydrated /etc/service && \
    ln -sfv /dev/stdout /var/log/nginx/access.log && \
    ln -sfv /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443
ENTRYPOINT ["usr/bin/start_runit"]
