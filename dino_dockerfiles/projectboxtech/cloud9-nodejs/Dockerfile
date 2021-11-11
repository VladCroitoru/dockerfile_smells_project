# Cloud9 server - a web based coding environment

# nodejs v8.9.4 is an LTS release
# According to NodeJS, v8.9.4 will be supported actively until April 2019 and maintained until December 2019.
FROM node:8.9.4-slim
MAINTAINER Jonathan Camenzuli <contact@projectbox.tech>

# get OS packages
RUN \
 buildDeps='make build-essential g++ gcc python2.7' \
 && softDeps="tmux git openssh-server zip unzip" \
 && apt-get update && apt-get upgrade -y \
 && apt-get install -y $buildDeps $softDeps --no-install-recommends

# get NPM packages
RUN \
 npm install -g forever

# get cloud9
RUN \
 git clone https://github.com/c9/core.git /cloud9 \ 
 && cd /cloud9 \
 && git reset --hard 58b6fa3d98be8a73ed10348ee5f5ec10601312c7 \
 && scripts/install-sdk.sh

# run server-side tests
RUN \
 cd /cloud9 \ 
 && npm run test

# cleanup
RUN \
 apt-get purge -y --auto-remove $buildDeps \
 && apt-get autoremove -y && apt-get autoclean -y && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && npm cache clean --force

ENV LEIN_ROOT true
 
VOLUME /workspace
EXPOSE 8181 
ENTRYPOINT ["forever", "/cloud9/server.js", "-w", "/workspace", "-l", "0.0.0.0"]

#CMD["--auth","username:password"]

