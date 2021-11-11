FROM node:6

RUN curl -sSL https://get.docker.com/ | sh && apt-get install docker-engine \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && npm install -g @angular/cli

WORKDIR /home/node
ENV NPM_CONFIG_LOGLEVEL info
