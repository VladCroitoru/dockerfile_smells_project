FROM gliderlabs/alpine:3.2
MAINTAINER pjpires@gmail.com

ADD binaries/logstash-forwarder /logstash-forwarder/logstash-forwarder

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --update upgrade && apk add runit && \
    rm -rf /var/cache/apk/*

# Certificates
VOLUME ["/logstash-forwarder/config"]
VOLUME ["/logstash-forwarder/certs"]

# Add configuration files
ADD logstash-forwarder.conf /logstash-forwarder/config/logstash-forwarder.conf

# Add runnable scripts
ADD run_logstash_forwarder.sh /etc/service/logstash-forwarder/run
RUN chmod u+x /etc/service/logstash-forwarder/run

CMD ["/sbin/runsvdir", "-P", "/etc/service"]
