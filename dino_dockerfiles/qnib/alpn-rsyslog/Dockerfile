FROM qnib/alpn-consul

ARG RSYSLOG_VER=8.16.0
ENV FORWARD_TO_ELASTICSEARCH=false \
    FORWARD_TO_KAFKA=false \
    FORWARD_TO_HEKA=false \
    FORWARD_TO_LOGSTASH=false \
    FORWARD_TO_FILE=false
ADD patch/rsyslog.h /tmp/
RUN apk add --update autoconf automake curl-dev g++ gnutls-dev json-c-dev libee-dev libestr-dev libgcrypt-dev liblogging-dev libnet-dev libtool make net-snmp-dev perl py-docutils tar util-linux-dev wget zlib-dev \
 && wget -qO - http://www.rsyslog.com/files/download/rsyslog/rsyslog-${RSYSLOG_VER}.tar.gz |tar xfz - -C /opt/ \
 && cd /opt/rsyslog-${RSYSLOG_VER} \
 && cat /tmp/rsyslog.h >> runtime/rsyslog.h \
 && ./configure --prefix=/usr/ --enable-elasticsearch --enable-imfile --enable-imptcp --enable-impstats --enable-mmjsonparse \
 && make \
 && make install \
 && apk del autoconf automake g++ libtool make tar wget \
 && rm -rf /var/cache/apk/*
ADD etc/supervisord.d/rsyslog.ini \
    etc/supervisord.d/rsyslog_conf.ini \
    /etc/supervisord.d/
ADD opt/qnib/rsyslog/bin/configure-targets.sh \
    opt/qnib/rsyslog/bin/start.sh \
    /opt/qnib/rsyslog/bin/
ADD etc/consul-templates/rsyslog_targets.conf.ctmpl /etc/consul-templates/
ADD etc/rsyslog.conf /etc/
ADD etc/conf.d/rsyslog /etc/conf.d/
ADD etc/consul.d/rsyslog.json /etc/consul.d/
ADD etc/rsyslog.d/file.conf.disabled \
    etc/rsyslog.d/heka.conf.disabled \
    etc/rsyslog.d/kafka.conf.disabled \
    etc/rsyslog.d/elasticsearch.conf.disabled \
    etc/rsyslog.d/logstash.conf.disabled \
    /etc/rsyslog.d/
