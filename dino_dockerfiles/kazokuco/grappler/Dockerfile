FROM golang:1.7

WORKDIR $GOPATH/src/github.com/kazokuco/grappler
ADD . .
RUN go get . && go install .
CMD ["grappler"]
