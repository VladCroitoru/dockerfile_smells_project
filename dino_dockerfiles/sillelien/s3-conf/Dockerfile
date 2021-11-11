FROM sillelien/base-alpine:0.9.2
VOLUME /conf
RUN apk -Uuv add openssl curl && rm /var/cache/apk/*
COPY run.sh /run.sh
RUN chmod 755 /run.sh
CMD /run.sh
ENV S3_CONF_SOURCE_FILE conf.yml
ENV S3_CONF_DEST_FILE conf.yml
