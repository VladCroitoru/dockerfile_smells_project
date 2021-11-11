FROM golang
ADD . /go/src/github.com/ThatsNinja/dockerhub-webhook-listener
ADD ./etc /etc/confd

WORKDIR /go/src/github.com/ThatsNinja/dockerhub-webhook-listener/hub-listener
RUN go get github.com/scalingdata/gcfg
RUN go build

# Add confd for configuration management
ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /usr/local/bin/confd
RUN chmod +x /usr/local/bin/confd

ENTRYPOINT ["/go/src/github.com/ThatsNinja/dockerhub-webhook-listener/bin/docker-entrypoint.sh"]
CMD /go/src/github.com/ThatsNinja/dockerhub-webhook-listener/hub-listener/hub-listener --config-file=/tmp/config.ini --listen=$listen_addr
