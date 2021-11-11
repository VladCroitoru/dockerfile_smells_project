FROM golang:1.5
MAINTAINER Eagle Chen <chygr1234@gmail.com>

COPY metrics.go /tmp/
COPY Godeps /tmp/Godeps
COPY docker-entrypoint.sh /

RUN \
  go get github.com/tools/godep && \
  cd /tmp && \
  godep go build && ls -lh && \
  mv tmp /usr/bin/river_metrics_transformer && \
  rm /tmp/metrics.go && rm -r /tmp/Godeps

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 12801

CMD ["-host", "0.0.0.0"]
