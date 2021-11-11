FROM geekupvn/docker-phalcon
MAINTAINER thinhvoxuan <thinhvoxuan@gmail.com>

RUN apt-get update && apt-get install -y apt-utils cron

ADD files/crontab /app/crontab
ADD files/bin/start-cron.sh /usr/bin/start-cron.sh
RUN chmod +x /usr/bin/start-cron.sh
RUN touch /var/log/cron.log

CMD /usr/bin/start-cron.sh

