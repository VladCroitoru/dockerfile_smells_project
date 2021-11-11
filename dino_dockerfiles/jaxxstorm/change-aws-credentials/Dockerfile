FROM golang:1.10.0-alpine3.7

WORKDIR /go/src/github.com/jaxxstorm/change-aws-credentials

COPY . .

RUN apk update && apk upgrade && \
    apk add --no-cache git

RUN go get -v github.com/Masterminds/glide

RUN cd $GOPATH/src/github.com/Masterminds/glide && git checkout tags/v0.12.3 && go install && cd -

RUN ls .

RUN glide install

RUN go build -o change-aws-credentials main.go

ENTRYPOINT ["./change-aws-credentials"] 
