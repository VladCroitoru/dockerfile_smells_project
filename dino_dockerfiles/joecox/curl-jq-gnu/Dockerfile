FROM alpine:3.5

ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 /usr/local/bin/jq-1.5

RUN chmod 0755 /usr/local/bin/jq* \
    && ln -s /usr/local/bin/jq-1.5 /usr/local/bin/jq \
    && ln -s /lib /lib64 \
    && ln -s /lib/ld-musl-x86_64.so.1 /lib/ld-linux-x86-64.so.2

RUN apk add --update curl coreutils && \
    rm -rf /var/cache/apk/*

CMD [ "sh" ]