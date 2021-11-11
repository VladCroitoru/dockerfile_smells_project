# Etherpad-Lite Dockerfile using SQLite as backend.
#
# https://github.com/kaergel/etherpad-docker

# Use Docker's nodejs, which is based on ubuntu
FROM node:13
LABEL maintainer="Thomas Kärgel, kaergel at b1-systems.de"

# You may overwrite the version. Use a Git branch or tag from https://github.com/ether/etherpad-lite.
ENV ETHERPAD_VERSION 1.8.0
ENV ETHERPAD_ADMIN_PASSWORD supersecret
ENV USERID 1000
ENV GROUPID 1000

# Get Etherpad-lite's other dependencies
RUN apt-get update \
  && apt-get install -y sqlite3 unzip gzip curl python libssl-dev pkg-config build-essential supervisor \
  && apt-get install -y abiword

WORKDIR /opt/

# Grab the latest Git version
RUN curl -SLO https://github.com/ether/etherpad-lite/archive/${ETHERPAD_VERSION}.zip \
  && unzip ${ETHERPAD_VERSION}.zip \
  && rm ${ETHERPAD_VERSION}.zip \
  && mv etherpad-lite-${ETHERPAD_VERSION} etherpad-lite

WORKDIR /opt/etherpad-lite

# Install node dependencies as well as the json command line tool for easy
# manipulating settings.json later.
RUN bin/installDeps.sh \
  && npm install sqlite3 \
  && rm settings.json

# Save original node_modules. May be needed in entrypoint.sh later.
RUN tar zcf node_modules.orig.tgz node_modules/

COPY entrypoint.sh /entrypoint.sh

# Add conf files
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD settings.json /opt/etherpad-lite/settings.json.master
ADD npmrc /usr/local/etc/npmrc

# Allow changes to settings.conf as well as the Sqlite database being persistent.
VOLUME /opt/etherpad-lite/var

# Modules added by the Admin UI should be persistent.
VOLUME /opt/etherpad-lite/node_modules

EXPOSE 9001
ENTRYPOINT ["/entrypoint.sh"]
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
