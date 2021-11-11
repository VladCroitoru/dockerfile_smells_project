FROM golang:1.6-alpine

RUN apk add --no-cache git && go get github.com/reactiveraven/ymlparse && rm -rf $GOPATH/src/* && apk del --no-cache git

ENTRYPOINT ["ymlparse"]
CMD []
