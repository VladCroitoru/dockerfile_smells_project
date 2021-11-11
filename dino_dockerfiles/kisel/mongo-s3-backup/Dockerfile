FROM mongo
ADD . /script
RUN apt-get update && apt-get install -y cron s3cmd && apt-get clean
ENTRYPOINT ["/script/start.sh"]
