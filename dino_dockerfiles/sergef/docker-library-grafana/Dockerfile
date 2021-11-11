FROM sergef/docker-library-alpine:3.7 as builder

ENV GOPATH /go

RUN apk add --no-cache \
    build-base \
    git \
    go@community \
    make \
    musl-dev \
    python \
    rpm@community \
    ruby \
    ruby-dev \
    tar \
    yarn@community \
  && gem install --no-ri --no-rdoc fpm

ENV BUILD_VERSION v5.0.4

ENV BUILD_PATH /go/src/github.com/grafana/grafana
ENV BUILD_GIT_URL https://github.com/grafana/grafana.git

WORKDIR ${BUILD_PATH}

RUN git clone ${BUILD_GIT_URL} -b ${BUILD_VERSION} ${BUILD_PATH} \
  && go run build.go build

RUN yarn install --pure-lockfile --no-progress \
  && go run build.go package latest

FROM sergef/docker-library-alpine:3.7

EXPOSE 3000

ENV BUILD_PATH /go/src/github.com/grafana/grafana

COPY --from=builder ${BUILD_PATH}/bin/grafana-cli /usr/sbin/grafana-cli
COPY --from=builder ${BUILD_PATH}/bin/grafana-server /usr/sbin/grafana-server
COPY --from=builder ${BUILD_PATH}/conf /etc/grafana
COPY --from=builder ${BUILD_PATH}/conf/sample.ini /etc/grafana/grafana.ini

COPY --from=builder ${BUILD_PATH}/conf /usr/share/grafana/conf
COPY --from=builder ${BUILD_PATH}/public /usr/share/grafana/public
COPY --from=builder ${BUILD_PATH}/scripts /usr/share/grafana/scripts
COPY --from=builder ${BUILD_PATH}/tools /usr/share/grafana/tools

ENTRYPOINT [ "/sbin/tini", "--", "/usr/sbin/grafana-server" ]
CMD [ "--homepath=/usr/share/grafana", \
  "--config=/etc/grafana/grafana.ini", \
  "cfg:default.log.mode=console", \
  "cfg:default.paths.data=/var/lib/grafana", \
  "cfg:default.paths.logs=/var/log/grafana", \
  "cfg:default.paths.plugins=/var/lib/grafana/plugins", \
  "cfg:default.paths.provisioning=/etc/grafana/provisioning" ]
