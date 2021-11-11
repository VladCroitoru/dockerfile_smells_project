FROM fluent/fluentd:v0.12-onbuild
MAINTAINER Benjamin Wulff <Benjamin.Wulff.de@ieee.org>

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \

 # cutomize following instruction as you wish
 && sudo gem install \
        fluent-plugin-secure-forward fluent-plugin-record-reformer\

 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem

EXPOSE 24284
