FROM golang:1.10.0

WORKDIR /go/src/github.com/syoya/resizer

COPY . .

RUN go get -u github.com/golang/dep/... && \
  go install .

CMD resizer
