FROM golang:1.17-alpine AS build-golang
RUN apk add --update \
    git \
    gcc \
    libc-dev
ENV CGO_ENABLED=0
COPY . /go/src/tproxy
WORKDIR /go/src/tproxy
RUN go mod download
RUN go install .

FROM alpine:latest as build-tailscale
WORKDIR /bin
COPY . ./
ENV TSFILE=tailscale_1.14.3_amd64.tgz
RUN wget https://pkgs.tailscale.com/stable/${TSFILE} && \
  tar xzf ${TSFILE} --strip-components=1

FROM alpine:latest AS tproxy
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY entrypoint.sh /bin/entrypoint.sh
COPY --from=build-golang /go/bin/tproxy /bin/tproxy
COPY --from=build-tailscale /bin/tailscaled /bin/tailscaled
COPY --from=build-tailscale /bin/tailscale /bin/tailscale
RUN mkdir -p /var/run/tailscale /var/cache/tailscale /var/lib/tailscale

LABEL Author="Michael Wilson"
ENTRYPOINT ["/bin/entrypoint.sh"]
EXPOSE 443