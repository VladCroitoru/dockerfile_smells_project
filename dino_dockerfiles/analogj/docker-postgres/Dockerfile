FROM centurylink/postgresql:9.3
MAINTAINER Jason Kulatunga <jason@thesparktree.com>

# Disable existing cron jobs
RUN rm -rf
  /etc/cron.daily/dpkg \
  /etc/cron.daily/apt \
  /etc/cron.daily/passwd \
  /etc/cron.daily/logrotate \
  /etc/cron.daily/upstart \
  /etc/cron.weekly/fstrim

# Install WAL-E dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    postgresql-server-dev-9.3 \
    postgresql-plpython-9.3 \
    postgresql-9.3-plv8 \
    libxml2-dev \
    libxslt1-dev \
    python-dev \
    python-pip \
    daemontools \
    libevent-dev \
    lzop \
    pv &&\
    /etc/init.d/postgresql stop &&\
    pip install six --upgrade &&\
    pip install wal-e

# Create directory for storing secret WAL-E environment variables
RUN umask u=rwx,g=rx,o= &&\
  mkdir -p /etc/wal-e.d/env &&\
  chown -R root:postgres /etc/wal-e.d

# Remove build dependencies and clean up APT and temporary files
RUN DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y wget &&\
  apt-get clean &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set default environment modes

# determines if the postgres server is configured as a leader or a follower.
# master nodes generate the backups and the logs (wal-e is running in archive mode)
# slave nodes can only consume logs, DEFAULT, this is so that if we forget to set the value we dont accidently clobber our backups
# this can be one of the following: ["leader", "follower"]
ENV DOCKER_POSTGRES_MODE follower

# determines if a wal-e database backup should be recovered before starting postgres.
# this can be one of the following: ["true", "false"]
ENV DOCKER_POSTGRES_RECOVER false #this can be one of the following: ["true", "false"]

# if DOCKER_POSTGRES_RECOVER is true, this value determines which backup is restored
# the latest, or a specific date. ['LATEST', eg. '2012-03-06 16:38:00']
ENV DOCKER_POSTGRES_RECOVER_FROM LATEST

# copy the wal-e crontab file
# Crontab that does a full backup daily at 2AM and deletes old backups (retaining 7 previous backups) at 3AM:
COPY ./cron/wal-e     /etc/cron.d/wal-e

# copy over the modified startup scripts
ADD scripts /scripts
RUN chmod +x /scripts/start.sh

# run periodic full backups with cron + WAL-E, via runit
CMD ["/sbin/my_init"]
