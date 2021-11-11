FROM golang:1.16 AS builder

WORKDIR /build

COPY go.mod go.sum /build/
RUN go mod download
RUN go mod verify

ENV CGO_ENABLED=0

COPY . /build/

RUN export VERSION="$(git describe --tags --always)" \
 && export LD_FLAGS="-w -X main.Version=${VERSION}" \
 && echo "-- TEST" \
 && go test ./... \
 && echo "-- BUILD" \
 && go install -tags netgo -ldflags "${LD_FLAGS}" .

FROM busybox
LABEL maintainer="Robert Jacob <xperimental@solidproject.de>"

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /go/bin/panik /bin/panik

USER nobody
EXPOSE 8080

ENTRYPOINT ["/bin/panik"]
