FROM fluent/fluentd:latest
MAINTAINER mookjpy@gmail.com

USER root

RUN /home/ubuntu/ruby/bin/gem install fluent-plugin-google-cloud --no-rdoc --no-ri

VOLUME /var/lib/docker/containers
VOLUME /fluentd/log

CMD /home/ubuntu/ruby/bin/fluentd \
    -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
