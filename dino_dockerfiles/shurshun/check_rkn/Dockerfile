FROM golang:1.12.5 AS BUILD

WORKDIR /app

ENV GO111MODULE=auto
ENV CGO_ENABLED=0
ENV GOOS=linux

COPY go.mod go.sum main.go ./

RUN go mod vendor

RUN go build -o check_rkn .

FROM alpine

RUN \
    apk add --no-cache --update \
        ca-certificates \
        tzdata \
        curl

COPY --from=BUILD /app/check_rkn /

ENTRYPOINT ["/check_rkn"]
CMD ["0.0.0.0:8020", "/db"]

VOLUME ["/db"]
