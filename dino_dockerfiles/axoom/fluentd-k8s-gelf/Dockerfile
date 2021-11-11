FROM fluent/fluentd:v0.12.33
LABEL maintainer="Andreas Bieber <andreas.bieber@axoom.com>"
USER root
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH

RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        ruby-dev \
        libffi-dev \
    && echo 'gem: --no-document' >> /etc/gemrc \
    && gem install fluent-plugin-secure-forward \
    && gem install fluent-plugin-record-reformer \
    && gem install fluent-plugin-gelf-hs \
    && gem install fluent-plugin-kubernetes_metadata_filter \
    && gem install fluent-plugin-detect-exceptions \
    && gem install fluent-plugin-multi-format-parser \
    && gem install fluent-plugin-prometheus \
    && apk del .build-deps \
    && gem sources --clear-all \
    && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

RUN mkdir -p /fluentd/etc/config.d 

# Copy configuration files
COPY ./conf/fluent.conf /fluentd/etc/

# Copy plugins
COPY plugins /fluentd/plugins/

# Environment variables
ENV FLUENTD_OPT=""
ENV FLUENTD_CONF="fluent.conf"
ENV GELF_PROTOCOL="tcp"
ENV GELF_PORT="12201"

# Run Fluentd
CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
