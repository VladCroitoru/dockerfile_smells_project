FROM alpine:3.6

RUN apk --no-cache --update add \
                            build-base \
                            ca-certificates \
                            libressl \
                            gzip \
                            ruby \
                            ruby-irb \
                            ruby-dev && \
    echo 'gem: --no-document' >> /etc/gemrc && \
    gem install oj json \
                fluent-plugin-ua-parser fluent-plugin-geoip-filter \
                fluent-plugin-ignore-filter \
                fluent-plugin-s3 fluent-plugin-elasticsearch \
                fluent-plugin-rewrite-tag-filter fluent-plugin-sentry \
                fluent-plugin-parser fluent-plugin-record-reformer && \
    gem install fluentd -v 0.14.23 && \
    apk del build-base ruby-dev && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /usr/lib/ruby/gems/*/cache/*.gem

ENV DOCKERIZE_VERSION v0.5.0

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p /etc/fluent/plugin && mkdir -p /data/buffer
COPY plugin /etc/fluent/plugin/

COPY fluent.tmpl /etc/fluent/fluent.tmpl

EXPOSE 10224
EXPOSE 24224
EXPOSE 10228

CMD ["dockerize", "-template", "/etc/fluent/fluent.tmpl:/etc/fluent/fluent.conf", "fluentd"]
