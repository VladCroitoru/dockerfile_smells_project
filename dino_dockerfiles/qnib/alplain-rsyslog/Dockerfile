ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/qnib/alplain-init

ENV ENTRYPOINTS_DIR=/opt/qnib/entry/ \
    FORWARD_TO_ELASTICSEARCH=false \
    FORWARD_TO_KAFKA=false \
    FORWARD_TO_HEKA=false \
    FORWARD_TO_LOGSTASH=false \
    FORWARD_TO_FILE=false \
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/qnib/consul/bin/ \
    ELASTICSEARCH_HOST=tasks.elasticsearch
ARG RSYSLOG_VER=8.29.0
ARG LIBRDKAFKA_VER=0.11.0

COPY patch/rsyslog.h /tmp/
RUN apk add --update autoconf \
                     automake \
                     bsd-compat-headers \
                     curl-dev \
                     g++ \
                     gnutls-dev \
                     json-c-dev \
                     libee-dev \
                     libestr-dev \
                     libfastjson-dev \
                     libgcrypt-dev \
                     liblogging-dev \
                     libnet-dev \
                     libtool \
                     linux-headers \
                     make \
                     net-snmp-dev \
                     perl \
                     py-docutils \
                     tar \
                     util-linux-dev \
                     wget \
                     zlib-dev \
 && wget -qO - http://www.rsyslog.com/files/download/rsyslog/rsyslog-${RSYSLOG_VER}.tar.gz |tar xfz - -C /opt/ \
 && cd /opt/rsyslog-${RSYSLOG_VER} \
 && cat /tmp/rsyslog.h >> runtime/rsyslog.h \
 && ./configure --prefix=/usr/ \
        --enable-elasticsearch \
        #--enable-omkafka \
        --enable-imfile \
        --enable-imptcp \
        --enable-impstats \
        #--enable-imczmq \
        #--enable-omczmq \
        #--enable-mmgrok \
        --enable-mmjsonparse \
 && make \
 && make install \
 && rm -rf /var/cache/apk/* /opt/rsyslog-${RSYSLOG_VER} /tmp/rsyslog.h
COPY opt/qnib/entry/*.sh /opt/qnib/entry/
COPY etc/rsyslog.conf /etc/
COPY etc/rsyslog.d/file.conf.disabled \
     etc/rsyslog.d/heka.conf.disabled \
     etc/rsyslog.d/kafka.conf.disabled \
     etc/rsyslog.d/logstash.conf.disabled \
     /etc/rsyslog.d/
COPY opt/qnib/rsyslog/etc/*.conf /opt/qnib/rsyslog/etc/
CMD ["/usr/sbin/rsyslogd", "-n"]
