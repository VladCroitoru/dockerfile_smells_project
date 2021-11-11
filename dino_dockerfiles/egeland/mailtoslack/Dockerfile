FROM golang:1-alpine as build

MAINTAINER Frode Egeland <egeland@gmail.com>

WORKDIR /go/src/app

RUN apk add --virtual buildstuff git --no-cache

COPY mailtoslack.go app.go

RUN go get && \
    go build -i

FROM golang:1-alpine

COPY --from=build /go/src/app/app /usr/local/bin/app

ENV PORT=2525
EXPOSE 2525

CMD ["/usr/local/bin/app"]
