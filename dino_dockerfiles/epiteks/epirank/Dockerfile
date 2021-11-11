FROM golang:1.8-alpine

WORKDIR /go/src/github.com/Epiteks/Epirank

COPY . .

RUN apk add --no-cache git \
    && go get -d -v . \
    && apk del git

# RUN apk add --update alpine-sdk

RUN apk add --no-cache gcc libc-dev \
    && go build . \
    && apk del gcc libc-dev

FROM alpine:3.6 

COPY --from=0 /go/src/github.com/Epiteks/Epirank/Epirank .

ENTRYPOINT ["/Epirank"]

EXPOSE 8080
