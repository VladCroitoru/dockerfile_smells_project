FROM waleedsamy/alpine-confd

RUN apk add --update nginx bash curl && rm -rf /var/cache/apk/*

COPY confd /etc/confd

ADD entrypoint.sh /entrypoint.sh

RUN mkdir /run/nginx

RUN chown -R  nginx:nginx /var/lib/nginx

EXPOSE 80

CMD ["/entrypoint.sh"]
