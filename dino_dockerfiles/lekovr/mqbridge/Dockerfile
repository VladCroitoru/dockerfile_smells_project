ARG GOLANG_VERSION

FROM golang:$GOLANG_VERSION as builder

# git used for app version fetch
RUN apk add --no-cache git build-base
# gcc g++

WORKDIR /opt/app

# Cached layer
COPY ./go.mod ./go.sum ./
RUN go mod download

# Sources dependent layer
COPY ./ ./
RUN CGO_ENABLED=0 go test -tags test -covermode=atomic -coverprofile=coverage.out ./...
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-X main.version=`git describe --tags --always`" -a ./cmd/mqbridge

FROM scratch

WORKDIR /
COPY --from=builder /opt/app/mqbridge .
ENTRYPOINT ["/mqbridge"]
