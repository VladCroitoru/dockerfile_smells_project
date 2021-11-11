FROM golang:1.5.3

RUN rm -f /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apt-get update && \
    apt-get install -y librados-dev apache2-utils && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/registry && touch /opt/registry/repositories

ENV DISTRIBUTION_DIR /go/src/github.com/docker/distribution
ENV GOPATH $DISTRIBUTION_DIR/Godeps/_workspace:$GOPATH
ENV DOCKER_BUILDTAGS include_rados include_oss include_gcs include_scs

WORKDIR $DISTRIBUTION_DIR
COPY . $DISTRIBUTION_DIR
COPY cmd/registry/config-scs.yml /etc/docker/registry/config.yml
RUN make PREFIX=/go clean binaries

VOLUME ["/var/lib/registry"]
EXPOSE 5000
ENTRYPOINT ["registry"]
CMD ["/etc/docker/registry/config.yml"]
