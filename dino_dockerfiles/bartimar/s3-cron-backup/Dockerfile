FROM debian

# Create fake chown so docker scripts won't fail (ugly)
RUN mv /bin/chown /bin/chown.disabled
COPY chown /bin/chown

# backups to Amazon S3
RUN apt-get update && apt-get install -y s3cmd cron && rm -rf /var/lib/apt/lists/*
COPY s3cfg /root/.s3cfg
COPY s3-backup.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["cron","-f"]
