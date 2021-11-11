FROM golang

#ADD . /go/src/github.com/docker/dockercloud-quickstart-go
ADD . /go/src/github.com/nobuking/dockercloud-sample-go
RUN go get gopkg.in/mgo.v2
RUN go install github.com/nobuking/dockercloud-sample-go

ENV NAME Everyone 

ENTRYPOINT /go/bin/dockercloud-sample-go

EXPOSE 80
