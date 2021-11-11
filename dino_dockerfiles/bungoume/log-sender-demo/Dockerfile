FROM ruby:2.3

RUN gem install foreman oj && \
    gem install fluentd -v 0.12.28 && \
    gem install fluent-plugin-ua-parser fluent-plugin-geoip-filter fluent-plugin-ignore-filter \
                fluent-plugin-forest fluent-plugin-s3 fluent-plugin-elasticsearch fluent-plugin-rewrite-tag-filter \
                fluent-plugin-parser fluent-plugin-record-reformer

RUN mkdir -p /etc/fluent/plugin && mkdir -p /data/buffer && mkdir /data/pos && mkdir /data/log
COPY plugin /etc/fluent/plugin/

COPY fluent.conf /etc/fluent/

CMD ["fluentd"]
