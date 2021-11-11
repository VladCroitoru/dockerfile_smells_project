FROM fluent/fluentd:latest-onbuild
MAINTAINER Bernd KLAUS <self@berndklaus.at>
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH

USER root
RUN apk --no-cache add sudo build-base ruby-dev && \

    sudo -u fluent gem install fluent-plugin-secure-forward fluent-plugin-pushover fluent-plugin-grep fluent-plugin-parser && \

    rm -rf /home/fluent/.gem/ruby/2.3.0/cache/*.gem && sudo -u fluent gem sources -c && \
    apk del sudo build-base ruby-dev
COPY ./fluent.conf /fluentd/etc/fluent.conf

EXPOSE 24224

USER fluent
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT -v
