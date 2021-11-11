FROM golang:wheezy
MAINTAINER Iain Mckay <me@iainmckay.co.uk>

ENV DEBIAN_FRONTEND noninteractive
ENV ETCD_KEY /varnish
ENV ETCD_PEER http://127.0.0.1:4001
ENV OUT_DIRECTORS /etc/varnish/directors.vcl
ENV OUT_VCL /etc/varnish/default.vcl
ENV VARNISH_ALLOCATION 100m
ENV VARNISH_SECRET /etc/varnish/secret

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD vcl /etc/varnish/vcl
ADD . /opt/heliumd

RUN apt-get update \
    && apt-get install -y supervisor varnish python-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install supervisor-stdout

RUN cd /opt/heliumd \
    && go get github.com/coreos/go-etcd/etcd \
    && go build heliumd.go

EXPOSE 80
EXPOSE 6082

ENTRYPOINT /usr/bin/supervisord
CMD ["-n"]
