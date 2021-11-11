FROM golang AS build-env-golang

COPY *.go Gopkg.* src/github.com/okzk/mackerel-metrics-collect-agent/

RUN cd src/github.com/okzk/mackerel-metrics-collect-agent/ \
  && go get -v github.com/golang/dep/cmd/dep \
  && dep ensure -v \
  && go install -v github.com/okzk/mackerel-metrics-collect-agent \
  && go get github.com/okzk/s3get


FROM debian

ADD https://mackerel.io/file/cert/GPG-KEY-mackerel-v2 /tmp/

RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates gnupg \
  && sh -c 'echo "deb http://apt.mackerel.io/v2/ mackerel contrib" > /etc/apt/sources.list.d/mackerel.list' \
  && apt-key add /tmp/GPG-KEY-mackerel-v2 \
  && apt-get update \
  && apt-get install -y --no-install-recommends mkr mackerel-agent-plugins \
  && apt-get clean \
  && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/*

COPY --from=build-env-golang /go/bin/mackerel-metrics-collect-agent /go/bin/s3get /usr/local/bin/
COPY startup.sh /usr/local/bin/

ENV CONF_S3_URI= \
  MKR_INSTALL_PACKAGE=

EXPOSE 2018
CMD ["startup.sh"]
