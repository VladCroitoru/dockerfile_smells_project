FROM ubuntu:latest
MAINTAINER Chad Fawcett me@chadf.ca
WORKDIR /directus-to-s3

# Install cron, mysql client, and AWS CLI
RUN apt-get update \
  && apt-get install -y cron python-pip python-dev build-essential \
    mysql-client \
  && pip install awscli==1.11.35

# Add files
ADD crontab crontab
ADD backup backup
ADD start start

# Register crontab
RUN crontab ./crontab

CMD [ "/directus-to-s3/start" ]
