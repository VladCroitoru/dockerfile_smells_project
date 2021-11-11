FROM golang AS build-env-golang

RUN git clone https://github.com/okzk/mackerel-plugin-ecs-task-metrics.git src/github.com/okzk/mackerel-plugin-ecs-task-metrics \
  && cd src/github.com/okzk/mackerel-plugin-ecs-task-metrics/ \
  && go get -v github.com/golang/dep/cmd/dep \
  && dep ensure -v \
  && go install -v github.com/okzk/mackerel-plugin-ecs-task-metrics


FROM debian

ADD https://mackerel.io/file/cert/GPG-KEY-mackerel-v2 /tmp/

RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates gnupg2 s3cmd \
  && sh -c 'echo "deb http://apt.mackerel.io/v2/ mackerel contrib" > /etc/apt/sources.list.d/mackerel.list' \
  && apt-key add /tmp/GPG-KEY-mackerel-v2 \
  && apt-get update \
  && apt-get install -y --no-install-recommends mackerel-agent \
  && apt-get clean \
  && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/*

COPY --from=build-env-golang /go/bin/mackerel-plugin-ecs-task-metrics /usr/local/bin/
COPY startup.sh /usr/local/bin/

ENV CONF_S3_URI= ID_S3_URI=
CMD ["startup.sh"]
