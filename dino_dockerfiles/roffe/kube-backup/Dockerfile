FROM alpine:3.6

# Install wget, cacerts, openssl, bash & jq
RUN apk add --no-cache --update \
        bash \
        ca-certificates \
        jq \
        openssl \
    && wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 -O /usr/local/bin/dumb-init \
    && wget https://dl.minio.io/client/mc/release/linux-amd64/mc -O /usr/local/bin/mc \
    && wget https://storage.googleapis.com/kubernetes-release/release/v1.9.2/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x \
        /usr/local/bin/mc \
        /usr/local/bin/kubectl \
        /usr/local/bin/dumb-init \
    && apk del --no-cache --update \
        ca-certificates \
        openssl \
    && rm -rf /var/cache/apk/*

COPY src /

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD [ "/backup.sh" ]