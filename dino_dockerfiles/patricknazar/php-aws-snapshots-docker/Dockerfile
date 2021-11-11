FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive
COPY sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends curl python-pip php5-cli
RUN pip install --upgrade --user awscli
RUN ln -s /root/.local/bin/aws /usr/local/bin/aws
RUN chmod +x /usr/local/bin/aws

# copy scripts
RUN mkdir /scripts
COPY snapshots.php /scripts
COPY ./scripts/* /scripts/
RUN chmod +x /scripts/run.sh

# copy cron
COPY ./crontab /etc/cron.d/php-aws-snapshots

RUN touch /var/log/cron.log
CMD ["/scripts/run.sh"]