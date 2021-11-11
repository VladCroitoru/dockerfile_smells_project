FROM golang:1.16.3-alpine AS builder

#ENV GOPATH /usr/src/app

CMD echo $GOPATH

WORKDIR /go/src/tcpproxy

RUN apk --no-cache add ca-certificates git

COPY main.go /go/src/tcpproxy/main.go
#RUN GO111MODULE=on go mod init . && go get -v ./...
RUN GO111MODULE=off CGO_ENABLED=0 GOOS=linux go build -v -a -installsuffix cgo -o tcpproxy .

FROM scratch


#EXPOSE 8023 8080
# Since we started from scratch, we'll copy the SSL root certificates from the builder
WORKDIR /usr/local/bin

COPY --from=builder /go/src/tcpproxy/tcpproxy .

# tcpproxy -l 0.0.0.0:29418 -r origin.server:29418
#CMD ["tcpproxy", "-l"]
