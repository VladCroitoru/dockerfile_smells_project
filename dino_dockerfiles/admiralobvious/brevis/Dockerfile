FROM golang:1.14.2-alpine as builder
MAINTAINER Alexandre Ferland <aferlandqc@gmail.com>

ENV GO111MODULE=on

WORKDIR /build

RUN apk add --no-cache git

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build ./cmd/brevis

FROM scratch
COPY --from=builder /build/brevis /brevis
COPY --from=builder /build/configs /configs

ENTRYPOINT ["/brevis"]

EXPOSE 1323
CMD ["--env-name", "prod"]
