FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends && \
    apt-get install -y curl apt-transport-https build-essential && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV NVM_DIR=/root/.nvm
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \
    && source ~/.nvm/nvm.sh