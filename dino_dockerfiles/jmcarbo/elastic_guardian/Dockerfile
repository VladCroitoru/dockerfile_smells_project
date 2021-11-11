FROM golang
ADD . /go/src/elastic_guardian
RUN cd /go/src/elastic_guardian && go get ./... && go install .
