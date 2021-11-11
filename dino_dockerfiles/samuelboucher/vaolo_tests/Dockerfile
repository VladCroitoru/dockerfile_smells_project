FROM ubuntu:14.04

# Update ubuntu, install curl, install git, install clean and install vim
RUN apt-get update && \
	apt-get install -y curl git wget nano python build-essential &&\
	apt-get clean

# Install Nnode version manager
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.6.0

# Install nvm with node and npm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh  | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# confirm installation
RUN node -v
RUN npm -v

# Install Ionic2
RUN npm install -g cordova ionic

RUN sudo sh -c "echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list" \
	&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - \
	&& sudo apt-get update \
	&& sudo apt-get install -y google-chrome-stable

RUN git clone https://github.com/samuelBoucher/vaolo_raisons_verts.git

WORKDIR vaolo_raisons_verts/Vaolo

COPY karma.conf.js test-config/karma.conf.js
COPY package.json package.json

RUN npm install
RUN npm install is-docker karma-junit-reporter

CMD timeout -k 60 60 npm test

