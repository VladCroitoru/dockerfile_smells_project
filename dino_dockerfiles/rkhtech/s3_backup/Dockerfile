######
## Purpose: Backup volume that's been attached.  
## Flow: Given a mounted directory, this will create a tar.gz file, and upload it to an s3 bucket
## Option: It also has the ability to restore any of the tar.gz files that have already been uploaded to s3.
## Option: I can also 'revert' the last restore to what it was prior to the restore.

FROM rkhtech/awscli
MAINTAINER Randy Hommel

ENV TZ=America/Los_Angeles
RUN apk add bc tzdata
RUN echo $TZ > /etc/localtime

ADD s3backup-entrypoint.sh /s3backup-entrypoint.sh
ADD restore /usr/local/bin/restore

ENTRYPOINT /s3backup-entrypoint.sh
