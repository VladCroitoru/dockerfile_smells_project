FROM mongo:3.4.14

# backups to Amazon S3
RUN apt-get update && apt-get install -y python-pip && apt-get install -y cron && rm -rf /var/lib/apt/lists/*
RUN pip install s3cmd
COPY s3cfg /root/.s3cfg

# entrypoint
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
