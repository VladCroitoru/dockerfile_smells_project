FROM alpine
MAINTAINER lorenzo@setale.me

RUN apk --no-cache add curl bash

COPY ./send_metric.sh /entrypoint

RUN chmod +x /entrypoint

ENV CACHET_BASE_URL ""
ENV CACHET_APIKEY ""
ENV METRIC_ID ""
ENV METRIC_VALUE "1"

ENTRYPOINT ["/entrypoint"]
