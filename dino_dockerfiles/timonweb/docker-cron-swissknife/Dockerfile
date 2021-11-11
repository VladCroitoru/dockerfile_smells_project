FROM alpine:latest
MAINTAINER tim@timonweb.com

RUN apk update \
&& apk add --no-cache dcron wget rsync libmagic bash py-pip  \
&& pip install --disable-pip-version-check --no-cache-dir python-magic s3cmd \
&& rm -rf /var/cache/apk/*

RUN mkdir -p /var/log/cron \
&& mkdir -m 0644 -p /var/spool/cron/crontabs \
&& touch /var/log/cron/cron.log \
&& mkdir -m 0644 -p /etc/cron.d

ADD /scripts/cron.sh /
ADD /scripts/entrypoint.sh /
ADD /scripts/get-container-id-by-label.sh /usr/local/bin/get-container-id-by-label
ADD /scripts/docker-exec-container-by-label.sh /usr/local/bin/docker-exec-container-by-label
ADD /scripts/backup-and-upload.sh /usr/local/bin/backup-and-upload

RUN chmod +x /cron.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /usr/local/bin/get-container-id-by-label
RUN chmod +x /usr/local/bin/docker-exec-container-by-label
RUN chmod +x /usr/local/bin/backup-and-upload

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/cron.sh"]