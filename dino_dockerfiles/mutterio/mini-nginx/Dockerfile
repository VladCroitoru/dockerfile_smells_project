FROM mutterio/mini-base

RUN apk --update add openssl-dev pcre-dev zlib-dev nginx && \
  rm -rf /tmp/src && \
  rm -rf /var/cache/apk/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
RUN chown -R nginx:nginx /var/lib/nginx
RUN chown -R nginx:nginx /usr/share/nginx
VOLUME ["/var/log/nginx"]

WORKDIR /etc/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
