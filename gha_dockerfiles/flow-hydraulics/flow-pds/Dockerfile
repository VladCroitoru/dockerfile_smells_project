FROM golang:alpine AS builder

RUN apk update && apk add --no-cache \
  ca-certificates \
  musl-dev \
  gcc \
  build-base \
  git

ENV GO111MODULE=on \
  CGO_ENABLED=1 \
  GOOS=linux \
  GOARCH=amd64

WORKDIR /build

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY . .

RUN ./build.sh

WORKDIR /dist

RUN cp /build/main .

FROM scratch

COPY --from=builder /dist/main /
COPY --from=builder /build/cadence-transactions /cadence-transactions

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
# Needed for flow-go/fvm/extralog
COPY --from=builder /tmp /tmp

ENTRYPOINT ["/main"]
