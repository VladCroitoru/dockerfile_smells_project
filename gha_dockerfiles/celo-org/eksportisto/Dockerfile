FROM golang:1.13-alpine as builder
WORKDIR /app
RUN apk add --no-cache make git gcc linux-headers musl-dev

# Download dependencies & cache them in docker layer
COPY go.mod .
COPY go.sum .
RUN go mod download

# needed for forno websocket connections
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

# Build project (this prevents re-downloading dependencies when go.mod/sum didn't change)
COPY . .
RUN go build -tags musl -o eksportisto .

FROM scratch

ENV HOME /root
COPY --from=builder /app/eksportisto /app/eksportisto
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

ENTRYPOINT [ "/app/eksportisto" ]