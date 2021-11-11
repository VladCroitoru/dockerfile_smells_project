###############################################################################
#### Run the build on alpine - istiod doesn't need more.
# Main docker images for istiod will be distroless and alpine.
FROM golang:1.16-alpine AS build-base

WORKDIR /ws
ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOPROXY=https://proxy.golang.org

RUN apk add --no-cache git

# With caching should avoid repeated downloads as long as the sum/mod don't change
COPY go.mod go.sum  ./
RUN go mod download

###############################################################################
FROM build-base AS build

COPY cmd ./cmd
COPY pkg ./pkg

# Runs in /go directory
RUN go build -a -ldflags '-extldflags "-static"' -o istiod ./cmd/istiod
RUN go build -a -ldflags '-extldflags "-static"' -o istiod-vm ./cmd/istio-agent

###############################################################################
### Container running the combined control plane, with an alpine base ( smaller than distroless but with shell )
### TODO: add a distroless variant.
### This image should work as a drop-in replacement for Pilot, Galley(MCP portion), WebhookInjector
### Citadel, Gallye/Validation remain as separate deployments.
FROM envoyproxy/envoy-alpine AS istio-control

COPY --from=build /ws/istiod /usr/local/bin/istiod

WORKDIR /
RUN mkdir -p /etc/certs && \
    mkdir -p /etc/istio/proxy && \
    mkdir -p /etc/istio/config && \
    mkdir -p /var/lib/istio/envoy && \
    mkdir -p /var/lib/istio/config && \
    mkdir -p /var/lib/istio/proxy && \
    chown -R 1337 /etc/certs /etc/istio /var/lib/istio

# Defaults
COPY ./var/lib/istio /var/lib/istio/
USER 1337:1337
ENTRYPOINT /usr/local/bin/istiod
