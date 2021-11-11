FROM xueshanf/awscli

ENV CRON_SCHEDULE="* * * * *" \
    S3_BUCKET_URL= \
    BACKUP_NAME=backup \
    BACKUP_DIR=

RUN touch /var/log/cron.log

CMD ([[ -n "${S3_BUCKET_URL}" && -n "BACKUP_DIR" ]] || (echo "Missing configuration variable" && false)) \
 && echo "${CRON_SCHEDULE}"' tar -czf - ${BACKUP_DIR} | aws s3 cp - "${S3_BUCKET_URL}/${BACKUP_NAME}-$(date -u +"%Y-%m-%dT%H:%M:%SZ").tar.gz" >> /var/log/cron.log 2>&1' > /etc/crontabs/root \
 && crond -L /var/log/cron.log \
 && tail -f /var/log/cron.log

