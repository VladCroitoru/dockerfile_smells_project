FROM alpine:3.3

# CLI
ENV VERSION 6.0.11

RUN apk --update add nodejs=4.3.2-r1 && npm install -g postcss@6.0.11 postcss-cli cssnano autoprefixer && rm -rf /var/cache/apk/*

ENTRYPOINT [ "postcss" ]
