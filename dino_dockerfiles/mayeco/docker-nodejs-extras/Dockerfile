FROM mayeco/docker-base

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
        nodejs-legacy \
        npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN npm install -g bower && npm install -g gulp && npm cache clean
