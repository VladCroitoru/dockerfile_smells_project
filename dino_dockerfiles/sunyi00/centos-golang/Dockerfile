FROM sunyi00/centos:1.0.0

RUN yum -y install golang \
    && yum -y clean all

RUN mkdir -p /go/src /go/bin && chmod -R 777 /go
ENV GOPATH /go
ENV PATH /go/bin:$PATH
WORKDIR /go
