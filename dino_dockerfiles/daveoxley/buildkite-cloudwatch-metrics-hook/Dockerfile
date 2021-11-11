FROM daveoxley/webhook
MAINTAINER Dave Oxley <buildkite-docker@oxley.email>

ENV SRCPATH ${GOPATH}/src/github.com/daveoxley/buildkite-cloudwatch-metrics-hook

RUN mkdir -p ${SRCPATH}
COPY publisher ${SRCPATH}/publisher
RUN mkdir /conf && \
    cd ${SRCPATH}/publisher && go get -d && go build -o /conf/publisher && \
    rm -rf ${GOPATH}

RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/
COPY hooks.json /conf/hooks.json
