FROM alpine:3.4

RUN apk add --no-cache build-base ruby-irb libffi-dev ruby ruby-dev curl  && \
    apk add --no-cache --repository https://dl-cdn.alpinelinux.org/alpine/edge/testing/ uselessd-dev && \
    gem install --no-rdoc --no-ri \
        fluentd \
        fluent-plugin-systemd \
        fluent-plugin-cloudwatch-logs \
        fluent-plugin-rewrite-tag-filter \
        fluent-plugin-record-modifier \
    && \
    apk del build-base ruby-dev libffi-dev

ADD run.sh /fluentd

CMD /fluentd
