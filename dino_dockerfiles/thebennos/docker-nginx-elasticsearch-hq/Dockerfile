FROM nginx:1.10-alpine

EXPOSE 80

ADD https://github.com/royrusso/elasticsearch-HQ/archive/v2.0.3.tar.gz /
RUN tar -xzf v2.0.3.tar.gz && unlink v2.0.3.tar.gz
RUN mv elasticsearch-HQ-* /app

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

ADD run.sh /
CMD ["sh", "/run.sh"]
