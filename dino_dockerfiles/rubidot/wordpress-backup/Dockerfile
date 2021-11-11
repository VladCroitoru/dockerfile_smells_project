FROM wordpress:cli-php7.1
USER root
COPY backup.sh /usr/local/bin/backup
COPY restore.sh /usr/local/bin/restore
RUN mkdir /backups
RUN chmod a+x /usr/local/bin/backup
RUN chmod a+x /usr/local/bin/restore
CMD ["backup"]
