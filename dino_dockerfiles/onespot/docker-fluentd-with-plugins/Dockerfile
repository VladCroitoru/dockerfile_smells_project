FROM fluent/fluentd:v1.0.2-onbuild

# below RUN includes plugin as examples elasticsearch is not required
# you may customize including plugins as you wish

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-cloudwatch-logs:0.4.2 \
        fluent-plugin-ec2-metadata:0.1.1 \
        fluent-plugin-datadog:0.9.6 \
        fluent-plugin-loggly:0.0.9 \
        fluent-plugin-input-gelf:0.2.0 \
        fluent-plugin-record-modifier:1.0.2 \
        fluent-plugin-rewrite-tag-filter:2.0.2 \
        fluent-plugin-route:1.0.0 \
        fluent-plugin-concat:2.1.0 \
        fluent-plugin-docker-format:0.2.3 \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem
