# Dockerfile for the PDC's Composer service
#
#
# Composer for aggregate data queries. Links to ComposerDb.
#
# Example:
# sudo docker pull mongo:3.2.9
# sudo docker pull hdcbc/composer
# sudo docker run -d --name composerDb -h composerDb --restart=always \
#   -v /path/for/composerDb/:/data/:rw \
#   mongo:3.2.9
# sudo docker run -d --name=composer -h composer --restart=always \
#   --link composerdb:composerdb \
#   -p 2774:22 \
#   -p 3002:3002 \
#   -v </path/>/composer:/config:rw \
#   hdcbc/composer
#
# Linked containers
# - Mongo database:  --link composerdb:composerdb
#
# External ports
# - AutoSSH:         -p <hostPort>:22
# - Web UI:          -p <hostPort>:3002
#
# Folder paths
# - config:          -v </path/>:/config/:rw
#
#
FROM phusion/passenger-ruby19
MAINTAINER derek.roberts@gmail.com


################################################################################
# System
################################################################################


# Environment variables, users and packages
#
ENV TERM xterm
ENV DEBIAN_FRONTEND noninteractive
RUN adduser --disabled-password --gecos '' autossh
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927; \
    echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" \
      | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list; \
    apt-get update; \
    apt-get install -y \
      lynx \
      mongodb-org-shell=3.2.9 \
      mongodb-org-tools=3.2.9; \
    apt-get autoclean; \
    apt-get clean; \
    rm -rf \
      /var/tmp/* \
      /var/lib/apt/lists/* \
      /tmp/* \
      /usr/share/doc/ \
      /usr/share/doc-base/ \
      /usr/share/man/


# SSH config
#
RUN rm -f /etc/service/sshd/down; \
  sed -i \
    -e 's/#HostKey \/etc/HostKey \/config/' \
    -e 's/^#AuthorizedKeysFile.*/AuthorizedKeysFile\t\/config\/authorized_keys/' \
    -e 's/#PermitRootLogin.*/PermitRootLogin no/' \
    /etc/ssh/sshd_config; \
  ( \
      echo ''; \
      echo '# Keep connections alive, 60 second interval'; \
      echo '# '; \
      echo 'Host *'; \
      echo 'ServerAliveInterval 60'; \
  ) | tee -a /etc/ssh/ssh_config


################################################################################
# Application
################################################################################


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN sed -i -e 's/localhost:27017/composerdb:27017/' config/mongoid.yml; \
    chown -R app:app /app/; \
    /sbin/setuser app bundle install --path vendor/bundle


################################################################################
# Runit Service Scripts
################################################################################


# Rails
#
RUN SRV=rails; \
    mkdir -p /etc/service/${SRV}/; \
    ( \
      echo '#!/bin/bash'; \
      echo '#'; \
      echo 'set -eu'; \
      echo ''; \
      echo ''; \
      echo '# Stop any old instances'; \
      echo '#'; \
      echo 'PIDFILE=/app/tmp/pids/server.pid'; \
      echo '[ ! -s ${PIDFILE} ]|| \'; \
      echo '  kill $( cat ${PIDFILE}) || true'; \
      echo ''; \
      echo ''; \
      echo '# Start rails, removing pidfile on exit or failure'; \
      echo '#'; \
      echo 'cd /app/'; \
      echo '/sbin/setuser app bundle exec rails server -p 3002 || \'; \
      echo '  rm ${PIDFILE}'; \
    )  \
      >> /etc/service/${SRV}/run; \
    chmod +x /etc/service/${SRV}/run


# delayed_job and config
#
RUN SRV=support; \
    mkdir -p /etc/service/${SRV}/; \
    ( \
      echo '#!/bin/bash'; \
      echo '#'; \
      echo 'set -eu'; \
      echo ''; \
      echo ''; \
      echo '# Handle ssh config, if necessary'; \
      echo '#'; \
      echo 'touch /config/authorized_keys'; \
      echo '[ -s /config/ssh_host_rsa_key ]|| \'; \
      echo '  ssh-keygen -b 4096 -t rsa -f /config/ssh_host_rsa_key -q -N ""'; \
      echo ''; \
      echo ''; \
      echo '# Stop any old instances'; \
      echo '#'; \
      echo 'PIDFILE=/app/tmp/pids/delayed_job.pid'; \
      echo '[ ! -s ${PIDFILE} ]|| \'; \
      echo '  kill $( cat ${PIDFILE}) || true'; \
      echo ''; \
      echo ''; \
      echo '# Start delayed job, removing pidfile on exit or failure'; \
      echo "#"; \
      echo 'cd /app/'; \
      echo '/sbin/setuser app bundle exec /app/script/delayed_job run || \'; \
      echo '  rm ${PIDFILE}'; \
    )  \
      >> /etc/service/${SRV}/run; \
    chmod +x /etc/service/${SRV}/run


################################################################################
# Cron and Scripts
################################################################################


# Create Mongo maintenance script and add to cron
#
RUN SCRIPT=/mongoMaintenance.sh; \
  ( \
    echo '#!/bin/bash'; \
    echo '#'; \
    echo 'set -eu'; \
    echo ''; \
    echo ''; \
    echo '# Mongo eval command with server, database and port'; \
    echo '#'; \
    echo 'EVAL="/usr/bin/mongo composerdb/query_composer_development --eval"'; \
    echo ''; \
    echo ''; \
    echo '# Set indexes to prevent duplicates'; \
    echo '#'; \
    echo '${EVAL} "db.endpoints.ensureIndex({ base_url : 1 }, { unique: true });"'; \
    echo '${EVAL} "db.queries.ensureIndex({ title : 1 }, { unique: true });"'; \
    echo '${EVAL} "db.users.ensureIndex({ username : 1 }, { unique: true });"'; \
    echo ''; \
    echo ''; \
    echo '# Maintenance account'; \
    echo '#'; \
    echo '${EVAL} '"'"'db.users.insert({ '; \
    echo '  "first_name" : "HDC", "last_name" : "Maintenance", "username" : '; \
    echo '  "maintenance", "email" : "admin@hdcbc.ca", "encrypted_password" : '; \
    echo '  "\$2a\$10\$mWm0Lp5dcbtX1IzH2C0ayOefiAxO7ZlNCPJqFT10ZlZBQeK31PnbW", '; \
    echo '  "agree_license" : true, "approved" : true, admin : "false" '; \
    echo '});'"'"; \
    echo ''; \
    echo '# Dump DB'; \
    echo '#'; \
    echo 'mongodump --host composerdb --db query_composer_development --out /private/'; \
  )  \
    >> ${SCRIPT}; \
  chmod +x ${SCRIPT}; \
  ( \
    echo '# Run database dump script (boot, 2 PST = 10 UTC)'; \
    echo '@reboot '${SCRIPT}; \
    echo '0 10 * * * '${SCRIPT}; \
  ) \
    | crontab -


################################################################################
# Volumes, ports and start command
################################################################################


# Ports and volumes
#
EXPOSE 2774 3002
VOLUME /config /private


# Run Command
#
CMD ["/sbin/my_init"]
