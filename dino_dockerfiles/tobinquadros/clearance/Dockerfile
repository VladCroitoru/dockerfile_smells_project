FROM golang:latest
MAINTAINER Tobin Quadros
LABEL id=clearance

COPY . /go/src/github.com/tobinquadros/clearance
WORKDIR /go/src/github.com/tobinquadros/clearance

RUN go get -u github.com/golang/dep/cmd/dep && dep ensure -v
RUN bin/install

EXPOSE 8000

ENTRYPOINT [ "./docker-entrypoint.sh" ]

CMD [ "/go/bin/clearance" ]
