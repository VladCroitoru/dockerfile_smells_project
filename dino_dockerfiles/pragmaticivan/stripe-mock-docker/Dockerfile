FROM golang:alpine

RUN apk add --update --no-cache git && \
    go get -v -u github.com/stripe/stripe-mock

EXPOSE 12111

ENTRYPOINT ["stripe-mock"]
