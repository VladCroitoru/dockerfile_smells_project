FROM ubuntu:16.10

MAINTAINER Saskia Hiltemann <zazkia@gmail.com>

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    DEBUG=false \
    GALAXY_WEB_PORT=10000 \
    NOTEBOOK_PASSWORD=none \
    CORS_ORIGIN=none \
    DOCKER_PORT=none \
    API_KEY=none \
    HISTORY_ID=none \
    REMOTE_HOST=none \
    GALAXY_URL=none

# install dependencies
RUN apt-get update && \
    apt-get install -y apt-utils && \
    apt-get install -y python-software-properties git python g++ make libssl-dev pkg-config build-essential redis-server && \
    apt-get install -y curl nodejs npm nginx net-tools procps python-pip

RUN ln -s /usr/bin/nodejs /usr/bin/node && \
    npm install -g forever child_process

# install ethercalc
RUN mkdir /ethercalc-install && cd /ethercalc-install && \
    git clone https://github.com/audreyt/ethercalc.git && \
    cd ethercalc && sed -i 's/"nodemailer": "\*"/"nodemailer": "2.7.2"/' package.json && \
    npm install -g

RUN pip install bioblend galaxy-ie-helpers

# make some changes to ethercalc to import and export data to galaxy history
ADD ./start.html /usr/local/lib/node_modules/ethercalc/start.html
ADD ./main.js /usr/local/lib/node_modules/ethercalc/main.js
ADD ./player.js /usr/local/lib/node_modules/ethercalc/player.js

# GIE setup
ADD ./proxy.conf /proxy.conf
ADD ./monitor_traffic.sh /monitor_traffic.sh
ADD ./startup.sh /startup.sh
ADD ./ethercalc_import.sh /ethercalc_import.sh
ADD ./galaxy_export.py /galaxy_export.py

RUN mkdir -p /import /run/nginx

EXPOSE 80

CMD /startup.sh
