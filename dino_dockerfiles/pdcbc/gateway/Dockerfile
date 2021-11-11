# Dockerfile for the HDC's Gateway Service
#
# Part of an Endpoint deployment
#
#
# Receives E2E formatted XML, stores deidentified in a pre-existing MongoDb
# container and responds to aggreate data queries.
#
# Requires pre-configured and pre-approved SSH keys.  Contact admin@pdcbc.ca.
#
# Example:
# sudo docker pull mongo:3.2.9
# sudo docker pull hdcbc/gateway:latest
# sudo docker run -d --restart=always --name=gateway_db \
#   -v <local path>:/data/db/ \
#   mongo:3.2.9
# sudo docker run -d --restart=always --name=gateway \
#   -v <local path>:/home/autossh/.ssh/ \
#   -e GATEWAY_ID=9999 \
#   -e DOCTOR_IDS=11111,22222,...,99999 \
#   --link gateway_db:database \
#   hdcbc/gateway:latest
#
#
FROM phusion/passenger-ruby19
MAINTAINER derek.roberts@gmail.com
LABEL org.label-schema.description="Part of an Endpoint deployment." \
  org.label-schema.license="GPL-3.0" \
  org.label-schema.name="HDC/hQuery Gateway" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="http://hdcbc.ca/" \
  org.label-schema.usage="See https://github.com/HDCbc/endpoint." \
  org.label-schema.vcs-url="https://github.com/HDCbc/gateway" \
  org.label-schema.vendor="Health Data Coalition" \
  org.label-schema.version="1.0.1"


################################################################################
# System
################################################################################


# Environment variables, users and packages
#
ENV TERM xterm
ENV DEBIAN_FRONTEND noninteractive
RUN adduser --disabled-password --gecos '' autossh
RUN apt-get update; \
    apt-get install --no-install-recommends -y \
      autossh\
      mongodb-clients; \
    apt-get autoclean; \
    apt-get clean; \
    rm -rf \
      /var/tmp/* \
      /var/lib/apt/lists/* \
      /tmp/* \
      /usr/share/doc/ \
      /usr/share/doc-base/ \
      /usr/share/man/


################################################################################
# Runit Service Scripts
################################################################################


# Rails
#
RUN SERVICE=rails;\
    mkdir -p /etc/service/${SERVICE}/; \
    SCRIPT=/etc/service/${SERVICE}/run; \
    ( \
      echo '#!/bin/bash'; \
      echo '#'; \
      echo 'set -eu'; \
      echo ''; \
      echo ''; \
      echo '# Set variables and populate providers.txt'; \
      echo '#'; \
      echo 'DOCTOR_IDS=${DOCTOR_IDS:-cpsid}'; \
      echo '/gateway/providers.sh add ${DOCTOR_IDS}'; \
      echo ''; \
      echo ''; \
      echo '# Stop any old instances'; \
      echo '#'; \
      echo 'PIDFILE=/gateway/tmp/pids/server.pid'; \
      echo '[ ! -s ${PIDFILE} ]|| \'; \
      echo '  kill $( cat ${PIDFILE} )|| true'; \
      echo ''; \
      echo ''; \
      echo '# Start Rails server, removing pidfile on exit or failure'; \
      echo '#'; \
      echo 'cd /gateway/'; \
      echo 'echo "Starting Rails"'; \
      echo '/sbin/setuser app bundle exec rails server -p 3001 || \'; \
      echo '  rm ${PIDFILE}'; \
    )  \
      >> ${SCRIPT}; \
    chmod +x ${SCRIPT}


# delayed job
#
RUN SERVICE=delayed_job;\
    mkdir -p /etc/service/${SERVICE}/; \
    SCRIPT=/etc/service/${SERVICE}/run; \
    ( \
      echo '#!/bin/bash'; \
      echo ''; \
      echo ''; \
      echo '# Stop any old instances'; \
      echo '#'; \
      echo 'PIDFILE=/gateway/tmp/pids/delayed_job.pid'; \
      echo '[ ! -s ${PIDFILE} ]|| \'; \
      echo '  kill $( cat ${PIDFILE} )|| true'; \
      echo ''; \
      echo ''; \
      echo '# Start delayed job, removing pidfile on exit or failure'; \
      echo '#'; \
      echo 'cd /gateway/'; \
      echo 'echo "Starting delayed_job"'; \
      echo '/sbin/setuser app bundle exec /gateway/script/delayed_job run || \'; \
      echo '  rm ${PIDFILE}'; \
    )  \
      >> ${SCRIPT}; \
    chmod +x ${SCRIPT}


# autossh tunnel and config
#
RUN SERVICE=autossh;\
    mkdir -p /etc/service/${SERVICE}/; \
    SCRIPT=/etc/service/${SERVICE}/run; \
    ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -eu"; \
      echo ""; \
      echo ""; \
      echo "# Set variables"; \
      echo "#"; \
      echo "GATEWAY_ID=\${GATEWAY_ID:-0}"; \
      echo "USE_QDEV=\${USE_QDEV:-no}"; \
      echo "#"; \
      echo "IP_PROD=\${IP_PROD:-142.104.128.120}"; \
      echo "IP_QDEV=\${IP_QDEV:-142.104.128.121}"; \
      echo "PORT_AUTOSSH=\${PORT_AUTOSSH:-2774}"; \
      echo "PORT_START_GATEWAY=\${PORT_START_GATEWAY:-40000}"; \
      echo "PORT_REMOTE=\`expr \${PORT_START_GATEWAY} + \${GATEWAY_ID}\`"; \
      echo ""; \
      echo ""; \
      echo "# Ensure autossh user's home directory permissions"; \
      echo "#"; \
      echo "chown -R autossh:autossh /home/autossh/"; \
      echo ""; \
      echo ""; \
      echo "# Check for SSH keys, create if necessary"; \
      echo "#"; \
      echo "if [ ! -s /home/autossh/.ssh/id_rsa.pub ]"; \
      echo "then"; \
      echo "  /sbin/setuser autossh ssh-keygen -b 4096 -t rsa -N \"\" -C ep\${GATEWAY_ID}-\$(date +%Y-%m-%d-%T) -f /home/autossh/.ssh/id_rsa"; \
      echo "fi"; \
      echo ""; \
      echo ""; \
      echo "# Start query dev autossh tunnel (can opt out), leave in background"; \
      echo "#"; \
      echo "if [ \${USE_QDEV} != no ]"; \
      echo "then"; \
      echo "  /sbin/setuser autossh /usr/bin/autossh \${IP_QDEV} -p \${PORT_AUTOSSH} -N -R \${PORT_REMOTE}:localhost:3001 \\"; \
      echo "    -o ServerAliveInterval=60 -o Protocol=2 -o StrictHostKeyChecking=no -f"; \
      echo "fi"; \
      echo ""; \
      echo ""; \
      echo "# Export PID variable and stop any autossh instances"; \
      echo "#"; \
      echo "export AUTOSSH_PIDFILE=/home/autossh/autossh.pid"; \
      echo "if [ -s \${AUTOSSH_PIDFILE} ]"; \
      echo "then"; \
      echo "  kill \$( cat \${AUTOSSH_PIDFILE}) || true"; \
      echo "  rm \${AUTOSSH_PIDFILE}"; \
      echo "fi"; \
      echo ""; \
      echo ""; \
      echo "# Start primary autossh tunnel, keep in foreground"; \
      echo "#"; \
      echo 'echo "Starting AutoSSH"'; \
      echo "/sbin/setuser autossh /usr/bin/autossh \${IP_PROD} -p \${PORT_AUTOSSH} -N -R \${PORT_REMOTE}:localhost:3001 \\"; \
      echo "  -o ServerAliveInterval=30 -o Protocol=2 -o ExitOnForwardFailure=yes -o StrictHostKeyChecking=no"; \
      echo ""; \
      echo ""; \
      echo "# If connection has failed, provide direction"; \
      echo "#"; \
      echo "cat /home/autossh/.ssh/id_rsa.pub"; \
      echo "echo"; \
      echo "echo 'AutoSSH not connected.  Please provide /home/autossh/.ssh/id_rsa.pub (above),'"; \
      echo "echo 'a list of participating CPSIDs and all paperwork to the PDC at admin@pdcbc.ca'"; \
      echo "sleep 60"; \
      )  \
        >> ${SCRIPT}; \
    	chmod +x ${SCRIPT}


################################################################################
# Cron and Maintenance Scripts
################################################################################


# SSH test
#
RUN SCRIPT=/ssh_test.sh; \
    ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -eu"; \
      echo ""; \
      echo ""; \
      echo "# Attempt to connect autossh tunnel and notify user"; \
      echo "#"; \
      echo "sleep 5"; \
      echo "echo"; \
      echo "echo"; \
      echo "if [ \"\$( setuser autossh ssh -p 2774 -o BatchMode=yes -o StrictHostKeyChecking=no 142.104.128.120 /app/test/ssh_landing.sh )\" ]"; \
      echo "then"; \
      echo "  echo 'Connection successful!'"; \
      echo "  echo"; \
      echo "  echo ':D'"; \
      echo "else"; \
      echo "  cat /home/autossh/.ssh/id_rsa.pub"; \
      echo "  echo 'ERROR: unable to connect to 142.104.128.120'"; \
      echo "  echo"; \
      echo "  echo 'Please verify the ssh public key (above) has been provided to admin@pdcbc.ca.'"; \
      echo "fi"; \
      echo "echo"; \
      echo "echo"; \
    )  \
      >> ${SCRIPT}; \
    chmod +x ${SCRIPT}


# MongoDb maintenance
#
RUN SCRIPT=/db_maintenance.sh; \
  ( \
    echo "#!/bin/bash"; \
    echo "#"; \
    echo "set -eu"; \
    echo ""; \
    echo ""; \
    echo "# Set index"; \
    echo "#"; \
    echo "/usr/bin/mongo database:27017/query_gateway_development --eval 'db.records.createIndex({ hash_id : 1 }, { unique : true })'"; \
    echo ""; \
    echo ""; \
    echo "# Database junk cleanup"; \
    echo "#"; \
    echo "/usr/bin/mongo database:27017/query_gateway_development --eval 'db.delayed_backend_mongoid_jobs.drop()'"; \
    echo "/usr/bin/mongo database:27017/query_gateway_development --eval 'db.providers.drop()'"; \
    echo "/usr/bin/mongo database:27017/query_gateway_development --eval 'db.queries.drop()'"; \
    echo "/usr/bin/mongo database:27017/query_gateway_development --eval 'db.results.drop()'"; \
  )  \
    >> ${SCRIPT}; \
  chmod +x ${SCRIPT}; \
  ( \
    echo "# Run maintenance script at boot and Sun 22 PST (= 6 UTC)"; \
    echo '@reboot '${SCRIPT}; \
    echo "0 6 * * Sun "${SCRIPT}; \
  ) \
    | crontab -


################################################################################
# Application
################################################################################


# Prepare /gateway/ folder, point mongoid.yml to container and run install
#
WORKDIR /gateway/
COPY . .
RUN sed -i 's/localhost/database/' config/mongoid.yml
RUN mkdir -p ./tmp/pids ./util/files; \
    gem install multipart-post; \
    chown -R app:app /gateway/; \
    /sbin/setuser app bundle install --path vendor/bundle


################################################################################
# Volumes, ports and start command
################################################################################


# Volumes
#
EXPOSE 3001
VOLUME /home/autossh/.ssh/
RUN chown -R autossh:autossh /home/autossh/


# Initialize
#
WORKDIR /
CMD ["/sbin/my_init"]
