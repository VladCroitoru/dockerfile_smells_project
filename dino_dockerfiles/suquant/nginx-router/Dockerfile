FROM alpine:3.2

# install common packages
RUN apk update && \
    apk add nginx curl &&\
    curl -o /usr/bin/confd -sSL \
        https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 && \
    chmod +x /usr/bin/confd && \
    mkdir -p /var/lib/nginx && \
    chmod -R a+rwx /var/lib/nginx

COPY bin/ /app/bin/
COPY confd/ /etc/confd/
COPY nginx.conf /etc/nginx/

VOLUME ["/var/lib/media"]
VOLUME ["/etc/nginx/shared"]

ENTRYPOINT ["/app/bin/entrypoint"]
CMD [""]

EXPOSE 80 443
