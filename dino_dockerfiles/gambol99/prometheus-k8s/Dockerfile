#
#   Author: Rohith
#   Date: 2015-07-23 12:00:34 +0100 (Thu, 23 Jul 2015)
#
#  vim:ts=2:sw=2:et
#
FROM progrium/busybox
MAINTAINER Rohith <gambol99@gmail.com>

ADD https://drone.io/github.com/gambol99/prometheus-k8s/files/bin/prometheus-k8s.gz /bin/prometheus-k8s.gz
RUN md5sum /bin/prometheus-k8s.gz && \
    gunzip /bin/prometheus-k8s.gz && \
    chmod +x /bin/prometheus-k8s

ENTRYPOINT [ "/bin/prometheus-k8s" ]
