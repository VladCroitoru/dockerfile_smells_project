FROM ubuntu:14.04

MAINTAINER nohona <nohona@hotmail.com>

LABEL version 1.0
LABEL description "Cron with mysql client db backup script, aws cli"

# Install pip and aws cli
RUN apt-get update && apt-get install -y python-pip \
        python-dev \
        build-essential \
        cron \
        mysql-client \
        wget \
        unzip \
        && pip install --upgrade pip \
        && pip install --upgrade --user awscli \
        && mkdir /mysql_scripts \
        && wget https://github.com/certbot/certbot/archive/master.zip -P /usr/local \
        && unzip /usr/local/master.zip -d /usr/local \
        && rm /usr/local/master.zip

COPY    ./docker/cron.scripts/dbbackup.sh /mysql_scripts
COPY    ./docker/cron.scripts/set-system-env.sh /mysql_scripts
COPY    ./docker/cron.scripts/crm-cron /etc/cron.d

# Make shell scripts executable, create cron.log file
RUN chmod +rx /mysql_scripts/*.sh \
    && touch /var/log/cron.log

WORKDIR /mysql_scripts

ENTRYPOINT ["./set-system-env.sh"]

# To build:
# docker build -t <user-name>/cron-crm:latest .

# To run:
# docker run -d -t -i -e MYSQL_ROOT_PASSWORD='<password>' \
#   -e MYSQL_HOST='<mysql-host-url>' \
#   -e MYSQL_DATABASE='<db-name>' -e MYSQL_USER='<db-user>' \
#   -e MYSQL_PASSWORD='<user-password>' -e S3_URL='<sr-url>' \
#   -e AWS_ACCESS_KEY_ID='<aws-key>' \
#   -e AWS_SECRET_ACCESS_KEY='<aws-secret>' \
#   --name cron-crm <dockerhub-user-name>/cron-crm:latest

# Container shell access:
# docker exec -it cron-crm bash
# docker logs cron-crm