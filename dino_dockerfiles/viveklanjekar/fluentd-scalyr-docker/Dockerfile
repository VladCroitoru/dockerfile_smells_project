FROM fluent/fluentd:v1.2-onbuild
LABEL maintainer "Vivek Lanjekar <vivek.lanjekar@gmail.com>"

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-elasticsearch \
        fluent-plugin-scalyr \
        fluent-plugin-s3 \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem
EXPOSE 24224 5140
