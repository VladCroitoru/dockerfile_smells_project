FROM buildpack-deps:trusty-curl

MAINTAINER Sebastian Otaegui <feniix@gmail.com>

COPY . /go/src/github.com/CiscoCloud/mesos-consul
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y golang git mercurial \
  && DEBIAN_FRONTEND=noninteractive apt-get autoclean clean \
	&& cd /go/src/github.com/CiscoCloud/mesos-consul \
	&& export GOPATH=/go \
	&& go get \
	&& go build -o /bin/mesos-consul \
	&& rm -rf /go \
  && cd / \
	&& DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y golang git mercurial \
  && DEBIAN_FRONTEND=noninteractive apt-get -y autoclean clean \
  && DEBIAN_FRONTEND=noninteractive apt-get -y autoremove \
  && rm -rf /var/lib/apt/lists/* 

ENTRYPOINT [ "/bin/mesos-consul" ]
