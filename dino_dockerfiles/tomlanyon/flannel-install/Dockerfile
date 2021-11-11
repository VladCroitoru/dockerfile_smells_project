FROM google/golang
MAINTAINER Tom Lanyon <tom@oneshoeco.com>

RUN go get github.com/tools/godep
RUN godep get github.com/coreos/flannel
RUN godep get github.com/kelseyhightower/flannel-route-manager

ADD ./install.sh /install.sh
RUN chmod +x /install.sh
WORKDIR /

CMD [ "/install.sh" ]
