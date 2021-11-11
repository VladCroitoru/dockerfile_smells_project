FROM alpine:latest
MAINTAINER Gergely Mentsik "gergely@mentsik.eu"

ENV CRON="0 0 * * *" \
    USERID=0 \
    GROUPID=0 \
    TAG="docker-backup" \
    STOP_CONTAINERS="all" \
    START_CONTAINERS="all" \
    INCREMENTAL="true" \
    TIMEZONE="Europe/Vienna" \
    SMB="false" \
    SMB_USER="" \
    SMB_PASSWORD="" \
    SMB_PATH="" \
    EMAIL_HOST_PORT="" \
    EMAIL_USER="" \
    EMAIL_PASS="" \
    EMAIL_USE_STARTTLS="NO" \
    EMAIL_FROM="Docktartar" \
    EMAIL_FROM_ADRESS="" \
    EMAIL_SUBJECT="Docktartar" \
    EMAIL_TO="" \
    TEMP_DIR="NO"

ADD bin/docktartar.sh /root/docktartar.sh
ADD bin/run.sh /root/run.sh
ADD bin/test-mail.sh /root/test-mail.sh

#RUN apt-get update && apt-get install -y bash docker tar grep tzdata cron \
RUN apk add --update bash docker tar pigz grep tzdata cifs-utils ssmtp \
    && mkdir /backupSource \
    && mkdir /backupTarget \
    && mkdir /backupTmp \
    && chmod 755 /root/run.sh \
    && chmod 755 /root/docktartar.sh \
    && chmod 755 /root/test-mail.sh \
    && touch /var/log/cron.log

ENTRYPOINT ["/root/run.sh"]
