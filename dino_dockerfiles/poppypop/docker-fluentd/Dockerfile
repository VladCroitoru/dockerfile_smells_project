FROM fluent/fluentd:onbuild

# below RUN includes plugin as examples elasticsearch is not required
# you may customize including plugins as you wish

RUN apk add --no-cache --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-elasticsearch \
		fluent-plugin-record-modifier \
		fluent-plugin-rewrite-tag-filter \
		fluent-plugin-concat \
		fluent-plugin-retag \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && apk add --no-cache tzdata \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem
