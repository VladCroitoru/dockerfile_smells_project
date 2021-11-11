FROM centos:centos7

ENV TELEGRAF_VERSION 0.13.0
ENV DOCKERIZE_VERSION v0.2.0
ENV INFLUXDB_HOST influxdb
ENV TELEGRAF_DB metrics
ENV TELEGRAF_USER metrics
ENV TELEGRAF_PASSWORD metrics
ENV TELEGRAF_INTERVAL 30s
ENV TELEGRAF_INTERVAL_FLUSH 25s
ENV TELEGRAF_INTERVAL_JITTER 5s

COPY ceph.repo /etc/yum.repos.d/ceph.repo

RUN yum install -y epel-release && \
    yum install -y python python-pip ceph && \
    yum install -y https://dl.influxdata.com/telegraf/releases/telegraf-${TELEGRAF_VERSION}.x86_64.rpm && \
    yum clean all -y && \
    pip install timeout-decorator

RUN curl -sL https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    | tar -C /usr/local/bin -xzv

COPY telegraf.tmpl /etc/telegraf/
COPY ceph-metrics.py /opt/
RUN chmod +x /opt/ceph-metrics.py

CMD dockerize -template /etc/telegraf/telegraf.tmpl:/etc/telegraf/telegraf.conf telegraf
