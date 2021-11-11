FROM fluent/fluentd:v1.12
USER root
# below RUN includes plugin as examples elasticsearch is not required
# you may customize including plugins as you wish

RUN apk add --update krb5-libs snappy && \
    apk add --update --virtual .build-deps libffi-dev \
        sudo build-base ruby-dev snappy-dev build-base libexecinfo automake autoconf libtool && \
    sudo gem install fluent-plugin-kafka \
                     fluent-plugin-influxdb \
                     fluent-plugin-rewrite-tag-filter \
                     fluent-plugin-record-modifier \
                     fluent-plugin-juniper-telemetry \
                     fluent-plugin-snmp \
                     fluent-plugin-elasticsearch \
                     fluent-plugin-retag \
                     bigdecimal \
                     zookeeper \
                     snappy \
                     extlz4 \
                     fluent-plugin-gelf-hs && \
    sudo gem sources --clear-all && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* \
           /usr/lib/ruby/gems/2.5.0/cache

ADD plugins /fluentd/plugins
