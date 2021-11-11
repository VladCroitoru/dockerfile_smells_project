FROM gliderlabs/alpine:3.3
MAINTAINER Thomas Lomas

RUN apk add --no-cache py-pip py-setuptools ca-certificates gnupg mysql-client
RUN pip install s3cmd
RUN rm -rf /var/cache/apk/*

ADD files/s3cfg /root/.s3cfg
ADD files/run.sh /root/run.sh
ADD files/backup.sh /root/backup.sh
RUN chmod +x /root/run.sh
RUN chmod +x /root/backup.sh

ENV BACKUP_SCHEDULE="0 3 * * *"
ENV AWS_BUCKET_LOCATION="US"

WORKDIR /root
CMD ["/root/run.sh"]

