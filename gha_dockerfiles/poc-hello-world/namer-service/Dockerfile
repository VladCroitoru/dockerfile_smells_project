FROM golang:1.17.3 AS builder

WORKDIR /build

COPY go.mod .
COPY go.sum .
RUN go mod download && go mod verify

ADD . .

RUN go build \
  -ldflags "-X main.BuildID=${VERSION}" \
  -o namer

WORKDIR /dist
RUN cp /build/namer ./namer

FROM ubuntu:focal-20211006 AS app
COPY --from=builder /dist/namer /namer
ENTRYPOINT ["/namer"]
