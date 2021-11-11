FROM alpine:3.7

ENV AWS_REGION=eu-west-1 \
    BACKUP_PATH= \
    S3_TMP=/tmp/s3cmd.zip \
    S3_ZIP=/tmp/s3cmd-master

RUN apk --no-cache add \
      mongodb-tools \
      curl \
      py-pip \
      python \
      pv \
 && pip install --upgrade \
      pip \
      python-dateutil \
 && curl -sSL --output ${S3_TMP} https://github.com/s3tools/s3cmd/archive/master.zip \
 && unzip -q ${S3_TMP} -d /tmp \
 && mv ${S3_ZIP}/S3 ${S3_ZIP}/s3cmd /usr/bin/ \
 && rm -rf /tmp/* \
 && mkdir /backup

COPY entrypoint.sh /usr/local/bin/entrypoint

CMD /usr/local/bin/entrypoint
