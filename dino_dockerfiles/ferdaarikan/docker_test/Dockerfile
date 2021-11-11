FROM ferdaarikan/ubuntu_blank:latest

MAINTAINER testuser

# Enable EPEL for Node.js
# RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install Node...
#RUN yum install -y npm

ENV DEBIAN_FRONTEND noninteractive

#RUN apt-get update
#RUN apt-get -qq update
#RUN apt-get install -y nodejs npm
# TODO could uninstall some build dependencies

# debian installs `node` as `nodejs`
#RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10


##installing new node
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#RUN apt-get install build-essential libssl-dev
RUN apt-get install -y curl git
#RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash

ENV NVM_DIR /usr/local/.nvm
ENV NODE_VERSION 6.9.0

RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && \
    cd $NVM_DIR && \
git checkout `git describe --abbrev=0 --tags`


RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# confirm installation
RUN node -v
RUN npm -v
#RUN nvm -v
#RUN nvm install 6.9.0


# Copy app to /src
COPY . /src

# Install app and dependencies into /src
RUN cd /src; npm install

EXPOSE 1337

CMD cd /src && node ./server_ld.js
