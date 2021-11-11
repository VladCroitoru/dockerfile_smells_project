# Dockerfile for the PDC's HAPI service
#
#
# Hub API used by the PDC's Hub API (HAPI).  Links to Auth, HubDB and DCLAPI.
#
# Example:
# sudo docker pull pdcbc/hapi
# sudo docker run -d --name=hapi -h hapi --restart=always \
#   --link auth:auth \
#   --link dclapi:dclapi \
#   --link hubdb:hubdb \
#   -v /pdc/data/config/groups/:/home/app/groups:rw
#   pdcbc/hapi
#
# Linked containers
# - Auth:            --link auth:auth
# - DCLAPI:          --link dclapi:dclapi
# - HubDB:           --link hubdb:hubdb
#
# Folder paths
# - authorized_keys: -v </path/>:/home/app/groups/:rw
#
# Modify default settings
# - DACS federation: -e DACS_FEDERATION=<string>
# -    jurisdiction: -e DACS_JURISDICTION=<string>
# - Node secret:     -e NODE_SECRET=<string>
# - Reject non-CA
#     certificates?: -e REJECT_NONCA_CERTS=<0/1>
#
#
FROM phusion/passenger-nodejs
MAINTAINER derek.roberts@gmail.com


# Packages
#
RUN apt-get update; \
    apt-get install -y \
      libkrb5-dev \
      python2.7; \
    apt-get clean; \
    rm -rf \
      /var/lib/apt/lists/* \
      /tmp/* \
      /var/tmp/*


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN chown -R app:app /app/; \
    /sbin/setuser app npm config set python /usr/bin/python2.7; \
    /sbin/setuser app npm install; \
    cd lib/util/; \
    npm install clone


# Create startup script and make it executable
#
RUN mkdir -p /etc/service/app/; \
    ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -e -o nounset"; \
      echo ""; \
      echo ""; \
      echo "# Environment variables"; \
      echo "#"; \
      echo "PORT_AUTH_C=\${PORT_AUTH_C:-3006}"; \
      echo "DACS_FEDERATION=\${DACS_FEDERATION:-pdc.dev}"; \
      echo "#"; \
      echo "export PORT=\${PORT_HAPI:-3003}"; \
      echo "export DCLAPI_URI=http://dclapi:\${PORT_DCLAPI:-3007}"; \
      echo "export NODE_TLS_REJECT_UNAUTHORIZED=\${REJECT_NONCA_CERTS:-0}"; \
      echo "export SECRET=\${NODE_SECRET:-notVerySecret}"; \
      echo "#"; \
      echo "export AUTH_CONTROL=https://auth:\${PORT_AUTH_C}"; \
      echo "export HAPI_GROUPS=\${HAPI_GROUPS:-/volumes/groups/groups.json}"; \
      echo "export MONGO_URI=mongodb://hubdb:27017/query_composer_development"; \
      echo "export ROLES=/etc/dacs/federations/\${DACS_FEDERATION}/roles"; \
      echo ""; \
      echo ""; \
      echo "# Copy groups.json if not present"; \
      echo "#"; \
      echo "mkdir -p /volumes/groups/"; \
      echo "[ -s /volumes/groups/groups.json ]|| \\"; \
      echo "  cp /app/groups.json /volumes/groups/"; \
      echo ""; \
      echo ""; \
      echo "# Start service"; \
      echo "#"; \
      echo "cd /app/"; \
      echo "/sbin/setuser app npm start"; \
    )  \
      >> /etc/service/app/run; \
    chmod +x /etc/service/app/run


# Run Command
#
CMD ["/sbin/my_init"]


# Ports and volumes
#
EXPOSE 3003
#
VOLUME /volumes/groups/
VOLUME /volumes/reports/


################################################################################
# + Query Importer repo
################################################################################


# Prepare query importer
#
WORKDIR /app/
RUN git clone https://github.com/pdcbc/queryImporter -b 0.2.2 ; \
    cd queryImporter; \
    npm config set python /usr/bin/python2.7; \
    npm update -g npm; \
    npm install


# Create startup script and make it executable
#
RUN SCRIPT=/app/queryImporter/import_queries.sh; \
    ( \
      echo "#!/bin/bash"; \
      echo "#"; \
      echo "set -e -o nounset"; \
      echo ""; \
      echo ""; \
      echo "# Environment variables"; \
      echo "#"; \
      echo "SKIP_INITS=\${SKIP_INITS:-true}"; \
      echo ""; \
      echo ""; \
      echo "# Run importer"; \
      echo "#"; \
      echo "cd /app/queryImporter/"; \
      echo "SKIP_INITS=\${SKIP_INITS} node index.js import --mongo-host=hubdb \
            --mongo-db=query_composer_development --mongo-port=27017"; \
    )  \
      >> ${SCRIPT}; \
    chmod +x ${SCRIPT}
