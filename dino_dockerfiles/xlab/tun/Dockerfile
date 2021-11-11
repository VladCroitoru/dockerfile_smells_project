FROM progrium/busybox
MAINTAINER Maxim Kupriianov <max@kc.vc>
ADD https://raw.githubusercontent.com/bagder/ca-bundle/master/ca-bundle.crt /etc/ssl/ca-bundle.pem
ADD https://dl.xlab.is/bin/linux/tun.gz /go/bin/tun.gz
RUN gunzip /go/bin/tun.gz && chmod +x /go/bin/tun

ENTRYPOINT ["/go/bin/tun"]
EXPOSE 5051
