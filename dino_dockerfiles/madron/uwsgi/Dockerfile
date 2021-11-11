FROM alpine:3.8

RUN    apk --no-cache add su-exec==0.2-r0 uwsgi-python3==2.0.17-r1 nginx==1.14.0-r0 \
    \
    # forward request and error logs to docker log collector
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY docker /docker/
COPY nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["/docker/entrypoint.sh"]
CMD ["nginx"]
