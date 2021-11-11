FROM golang:1.9.2-alpine3.7
WORKDIR /go/src/app
COPY . .
RUN apk add --update --no-cache --virtual git && \
    go-wrapper download && \
    go-wrapper install && \
    apk del --purge git
CMD ["go-wrapper", "run"]