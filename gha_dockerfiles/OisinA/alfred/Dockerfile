FROM golang:1.17.1
ENV GO111MODULE=on

WORKDIR /alfred

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

FROM alpine as certs
RUN apk update && apk add ca-certificates

FROM scratch
COPY --from=1 /etc/ssl/certs /etc/ssl/certs
COPY --from=0 /alfred/alfred .
ENTRYPOINT [ "./alfred" ]