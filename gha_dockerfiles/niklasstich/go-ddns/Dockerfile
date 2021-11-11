# Build
FROM golang:latest AS build

WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download

COPY *.go .

RUN CGO_ENABLED=0 go build -ldflags '-s' -o  /go-ddns

FROM alpine:latest

WORKDIR /

COPY --from=build /go-ddns /go-ddns

ENTRYPOINT ["/go-ddns"]