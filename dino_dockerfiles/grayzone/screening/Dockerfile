FROM grayzone/beego

MAINTAINER Albert Wang


# Install Database libs
RUN go get -u -v github.com/lib/pq
RUN go get -u -v github.com/mattn/go-sqlite3



ADD . /go/src/github.com/grayzone/screening

WORKDIR /go/src/github.com/grayzone/screening

RUN go build github.com/grayzone/screening

RUN rm -rf /go/src/github.com/grayzone/screening/.git
RUN rm -rf /go/src/github.com/grayzone/screening/controllers
RUN rm -rf /go/src/github.com/grayzone/screening/routers
RUN rm -rf /go/src/github.com/grayzone/screening/models
RUN rm -rf /go/src/github.com/grayzone/screening/tests
RUN rm -rf /go/src/github.com/grayzone/screening/main.go

RUN rm -rf /go/src/github.com/grayzone/screening/Dockerfile
RUN rm -rf /go/src/github.com/grayzone/screening/docker-compose.yml

EXPOSE 8080

ENTRYPOINT ["/go/src/github.com/grayzone/screening/screening"]

