FROM alpine:3.9.2

ENV AWSCLI_VERSION "1.10.38"
ENV PACKAGES "groff less python py-pip curl openssl ca-certificates mysql-client bash findutils jq"

RUN apk add --update $PACKAGES \
    && pip install awscli==$AWSCLI_VERSION \
    && apk --purge -v del py-pip \
    && rm -rf /var/cache/apk/*

ADD ./assets/dump_database.sh /usr/local/bin/
RUN test -x /usr/local/bin/dump_database.sh

ADD ./assets/sync_to_s3.sh /usr/local/bin/
RUN test -x /usr/local/bin/sync_to_s3.sh

ADD ./assets/datadog-notify.sh /usr/local/bin/
RUN test -x /usr/local/bin/datadog-notify.sh

ADD ./assets/datadog_event_finished.sh /usr/local/bin/
RUN test -x /usr/local/bin/datadog_event_finished.sh

ADD ./assets/default_command.sh /usr/local/bin/
RUN test -x /usr/local/bin/datadog_event_finished.sh

CMD [ "/usr/local/bin/default_command.sh" ]
