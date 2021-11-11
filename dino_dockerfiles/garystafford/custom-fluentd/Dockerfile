FROM fluent/fluentd:v0.14.15-onbuild

LABEL MAINTAINER "Gary A. Stafford <garystafford@rochester.rr.com>"
ENV REFRESHED_AT 2017-09-26

USER root

RUN mkdir -p /home/fluent/docker/ \
  && chmod -R 775 /home/fluent/docker/ \
  && apk update \
  && apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
  && sudo -u fluent gem install \
        fluent-plugin-copy_ex \
        fluent-plugin-elasticsearch \
        fluent-plugin-concat \
  && sudo -u fluent gem sources --clear-all \
  && apk del .build-deps \
  && rm -rf /var/cache/apk/* \
        /home/fluent/.gem/ruby/2.3.0/cache/*.gem

USER fluent
