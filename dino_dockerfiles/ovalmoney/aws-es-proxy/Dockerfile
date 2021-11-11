FROM golang:1.9.2-alpine3.6

RUN addgroup -g 1000 golang \
    && adduser -u 1000 -G golang -s /bin/sh -D golang

RUN apk add --no-cache git

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download
RUN go-wrapper install
RUN go build -o aws-es-proxy

USER golang

ENV PORT 9200
ENV AWS_ES_HOST https://dummy-host.eu-west-1.es.amazonaws.com

EXPOSE ${PORT}

CMD ["/bin/sh", "-c", "./aws-es-proxy -listen 0.0.0.0:$PORT -endpoint $AWS_ES_HOST"]
