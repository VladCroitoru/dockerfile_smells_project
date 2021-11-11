FROM golang
ADD . /go/src/github.com/rynr/offer
RUN go get github.com/rynr/offer
RUN go install github.com/rynr/offer
ENTRYPOINT /go/bin/offer
EXPOSE 8080
