FROM ubuntu:bionic
MAINTAINER Jan Blaha

RUN apt-get update && apt-get install -y curl sudo git gnupg bzip2 && \
    apt-get update && \
    apt-get install -y --no-install-recommends docker.io && \
    # cleanup
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* && \
    rm -rf /src/*.deb

RUN mkdir -p /usr/src/app
RUN rm -rf /tmp/*

ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 12.16.1

# node
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash && \
    /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

WORKDIR /usr/src/app

COPY package.json /usr/src/app/

RUN npm install --production && \
    npm cache clean -f && \
    rm -rf /tmp/*

RUN mkdir /tmp/jsreport

COPY . /usr/src/app
COPY patch /usr/src/app

EXPOSE 5488

HEALTHCHECK CMD curl --fail http://localhost:5488 || exit 1

CMD [ "node", "index.js" ]
