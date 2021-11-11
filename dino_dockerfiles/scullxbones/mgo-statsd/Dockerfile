FROM golang:1.9 AS build-env

ENV DEP_VERSION v0.4.1
ENV GOOS linux
ENV GOARCH 386

RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/${DEP_VERSION}/dep-linux-amd64 && \
    chmod +x /usr/local/bin/dep
WORKDIR /go/src/github.com/scullxbones/mgo-statsd/

COPY . ./
RUN chmod +x build.sh && \
    ./build.sh

FROM alpine:3.7
WORKDIR /app
COPY --from=build-env /go/src/github.com/scullxbones/mgo-statsd/mgo-statsd /app/
ENTRYPOINT [ "./mgo-statsd" ]
CMD [ "--help" ]
