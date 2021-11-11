FROM alpine:3.12

RUN apk --no-cache add python3 py3-pip && \
    pip install awscli && \
    mkdir -p /data

ADD s3backup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/s3backup.sh && \
    ln -s /usr/local/bin/s3backup.sh /usr/local/bin/backup && \
    ln -s /usr/local/bin/s3backup.sh /usr/local/bin/show && \
    ln -s /usr/local/bin/s3backup.sh /usr/local/bin/stop

ENTRYPOINT ["/bin/sh","/usr/local/bin/s3backup.sh"]
CMD ["schedule"]
