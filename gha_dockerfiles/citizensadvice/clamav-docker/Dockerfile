FROM krallin/ubuntu-tini:xenial

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y -qq curl clamav clamav-daemon clamav-freshclam wget gettext-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /var/run/clamav && \
    touch /etc/clamav/clamd.conf && \
    touch /etc/clamav/freshclam.conf && \
    chown -R clamav:clamav /var/run/clamav /etc/clamav && \
    chmod 640 /etc/clamav/*.conf && \
    chmod 750 /var/run/clamav

EXPOSE 3310

ADD bootstrap.sh /
ADD clamd.conf.template /etc/clamav/
ADD freshclam.conf.template /etc/clamav/

RUN freshclam --verbose

ENV MAX_THREADS 12
ENV MAX_CONNECTION_QUEUE_LENGTH 15
ENV MAX_QUEUE=100
ENV MAX_SCAN_SIZE 100M
ENV MAX_FILE_SIZE 100M
ENV MAX_STREAM_LENGTH 100M

RUN for i in `find / -user clamav`; do chown 1000 $i; done && \
    usermod -u 1000 clamav

USER 1000

CMD ["/bootstrap.sh"]
