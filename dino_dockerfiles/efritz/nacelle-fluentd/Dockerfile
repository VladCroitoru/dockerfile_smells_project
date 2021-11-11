FROM fluent/fluentd:v0.12

RUN apk update && \
    apk add --update gettext && \
    gem install fluent-plugin-elasticsearch --no-rdoc --no-ri --version 1.9.2

EXPOSE 24224
ADD fluent.conf /fluentd/etc/fluent.conf.in
ADD startup.sh /
CMD /startup.sh
