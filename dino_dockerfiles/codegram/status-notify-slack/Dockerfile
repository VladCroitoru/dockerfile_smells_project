FROM alpine
MAINTAINER David Morcillo <david.morcillo@codegram.com>

ENV STATUS_URL "http://example.org"
ENV STATUS_TIMEOUT 1
ENV NOTIFY_TIMEOUT 5
ENV SLACK_CHANNEL "#example"
ENV SLACK_USERNAME "example"
ENV SLACK_USERNAME_OK "example"
ENV SLACK_NOTIFICATION_TEXT "This is an example text"
ENV SLACK_NOTIFICATION_TEXT_OK "This is an example text"
ENV SLACK_NOTIFICATION_ICON ":broken_heart:"
ENV SLACK_NOTIFICATION_ICON_OK ":green_heart:"
ENV SLACK_NOTIFICATION_WEBHOOK_URL "http://example.org"
ENV CURL_MAX_TIMEOUT 30
ENV MAX_FAILS_ALLOWED 3

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

ADD entry-point.sh .

ENTRYPOINT sh ./entry-point.sh

