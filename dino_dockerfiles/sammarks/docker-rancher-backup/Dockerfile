FROM ubuntu:15.10
MAINTAINER Samuel Marks sam@sammarks.me

# Install packages.
RUN apt-get update \
    && apt-get install -y -q --no-install-recommends \
        jq apt-transport-https ca-certificates cron \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo "deb https://apt.dockerproject.org/repo ubuntu-wily main" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y -q --no-install-recommends docker-engine \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

# Set some environment variables.
ENV DOCKER_HOST unix:///tmp/docker.sock
WORKDIR /backup/

# Copy files and set working directory.
ADD . /backup/

# Copy the crontab to the proper location.
RUN cp /backup/crontab /etc/cron.d/backup-cron \
    && chmod 0644 /etc/cron.d/backup-cron \
    && touch /var/log/cron.log \
    && chmod a+x /backup/backup.sh

# Set the entry point.
CMD /backup/backup.sh && cron && tail -f /var/log/cron.log
