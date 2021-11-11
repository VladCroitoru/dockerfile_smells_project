FROM alpine:3.2

RUN apk --update add bash bc logrotate && \
    rm -rf /var/cache/apk/*

ADD scripts /root/scripts

ADD conf/logrotate /etc/logrotate.d/utilization

RUN touch /var/log/utilization.log

RUN ln -s /root/scripts/utilization.sh /usr/local/bin/utilization

CMD ["tail", "-f", "/var/log/utilization.log"]
