FROM golang:alpine
ADD . /go/src/github.com/elsudano/MiddleWare_NextCloud
RUN go install github.com/elsudano/MiddleWare_NextCloud
CMD ["/go/bin/MiddleWare_NextCloud"]
EXPOSE 8080
