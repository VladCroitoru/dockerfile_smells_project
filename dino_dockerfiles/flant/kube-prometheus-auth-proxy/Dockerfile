FROM nginx:1.16.1-alpine

RUN apk add openssl --update && \
    rm -rf /var/cache/apk/* && \
    rm -rf /etc/nginx/*

COPY run-proxy /bin/run-proxy

ENTRYPOINT ["/bin/run-proxy"]
