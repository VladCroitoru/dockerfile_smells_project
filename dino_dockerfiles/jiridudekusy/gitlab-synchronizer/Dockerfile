FROM ubuntu:latest
MAINTAINER Jiří Dudek <jiri.dudek@unicorn.com>

RUN apt-get update && apt-get -y install cron git moreutils
COPY synchronize.sh /bin
# Add crontab file in the cron directory
ADD cron-jobs /etc/cron.d/synchronize-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/synchronize-cron

RUN git config --global http.sslVerify "false"

COPY start.sh /
# Run the command on container startup
CMD /start.sh
