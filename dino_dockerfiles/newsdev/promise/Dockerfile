FROM golang:1.4.2
RUN go get github.com/tools/godep
COPY . /go/src/github.com/newsdev/promise
WORKDIR /go/src/github.com/newsdev/promise
RUN godep go install .
ENTRYPOINT ["promise"]
