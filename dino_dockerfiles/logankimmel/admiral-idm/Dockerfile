FROM golang:1.7
ADD . /go/src/main
WORKDIR /go/src/main
RUN cd /go/src/main && go get ./...
CMD ["go", "run", "main.go"]
EXPOSE 8080
