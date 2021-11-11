FROM golang:1.11-stretch as build

RUN mkdir -p /exoip
ADD . /exoip
WORKDIR /exoip

RUN cd /exoip \
 && CGO_ENABLED=0 GOOS=linux go build -mod vendor -o exoip -ldflags "-s -w" github.com/exoscale/exoip/cmd/exoip


FROM linuxkit/ca-certificates:v0.6

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.name="ExoIP" \
      org.label-schema.vendor="Exoscale" \
      org.label-schema.description="IP watchdog" \
      org.label-schema.url="https://github.com/exoscale/exoip" \
      org.label-schema.schema-version="1.0"



COPY --from=build /exoip/exoip exoip

ENTRYPOINT ["./exoip", "-O"]
