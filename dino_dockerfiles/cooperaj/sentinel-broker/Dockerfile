# Build sentinel-broker binary
FROM golang:1.9 AS build-env

ADD . /go/src/github.com/cooperaj/sentinel-broker
WORKDIR /go/src/github.com/cooperaj/sentinel-broker

RUN go get -u github.com/golang/dep/cmd/dep \
    && dep ensure -vendor-only \
    && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o app .

# Run image
FROM scratch

ARG BUILD_DATE
ARG VCS_REF

LABEL maintainer="Adam Cooper <adam@networkpie.co.uk>" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.name="Sentinel Broker" \
      org.label-schema.vcs-url="https://github.com/cooperaj/sentinel-broker.git" \
      org.label-schema.version="0.8.9" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF

COPY --from=build-env /go/src/github.com/cooperaj/sentinel-broker/app /app/sentinel-broker
COPY --from=build-env /go/src/github.com/cooperaj/sentinel-broker/sentinel-config.json /app/sentinel-config.json

WORKDIR /app
EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=2s --start-period=20s \
    CMD wget -q http://localhost:8080/healthcheck || exit 1

CMD ["./sentinel-broker"]

ONBUILD ADD ./sentinel-config.json /app/sentinel-config.json
