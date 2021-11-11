FROM golang:1.9.1-alpine3.6

LABEL maintainer="Tobias Germer"

WORKDIR /go/src/app
COPY . .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN go-wrapper download
RUN go-wrapper install

EXPOSE 8080

CMD ["go-wrapper", "run"] 
