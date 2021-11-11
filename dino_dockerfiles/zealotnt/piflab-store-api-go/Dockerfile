FROM golang:latest

WORKDIR /go/src/github.com/o0khoiclub0o/piflab-store-api-go

ADD . ./
RUN go get github.com/tools/godep
RUN godep restore

ENV PORT 80
EXPOSE 80

RUN go install
CMD piflab-store-api-go

# For development
RUN go get bitbucket.org/zealotnt/goose/cmd/goose
RUN go get github.com/zealotnt/gin
RUN go get github.com/onsi/ginkgo
RUN go install github.com/onsi/ginkgo
RUN go get golang.org/x/tools/cmd/cover
RUN go get github.com/mattn/goveralls
RUN chmod +x ./testcoverage.sh

