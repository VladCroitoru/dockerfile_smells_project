FROM invokr/cgit

RUN yum update -y && yum upgrade -y && yum install go -y
RUN mkdir -p /go/src/reloader
ADD main.go /go/src/reloader/main.go
ENV GOPATH /go
RUN go get reloader


CMD /go/bin/reloader