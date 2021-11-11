FROM golang:alpine

# Update package index and install go + git
RUN apk add --update git
RUN apk add --no-cache bash gawk sed grep bc coreutils openssl ca-certificates certbot
RUN update-ca-certificates
RUN apk add --no-cache binutils make
RUN go get github.com/barnybug/s3
WORKDIR /go/src/github.com/barnybug/s3
RUN make
WORKDIR /go

ENV GOROOT /usr/local/go
ENV GOPATH /go

RUN ulimit -n 100000
ADD . /go

# expose port 8080
EXPOSE 8080

RUN go get -v github.com/dtannen/sseserver
RUN go build -o pinion_sse
ENTRYPOINT ["/bin/bash","-c"]
CMD ["./run.sh"]
