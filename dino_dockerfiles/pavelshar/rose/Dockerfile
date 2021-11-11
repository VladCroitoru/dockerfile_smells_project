FROM pavelshar/cassandra


# Use root user
USER root


# Copy deploy files into .docker folder
ADD . /.docker


# Build project
# Install and configure dependencies

# nvm environment variables
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.9.4


RUN \
    rm /bin/sh && ln -s /bin/bash /bin/sh && \
    sh /.docker/deploy/build/php.sh && \
    sh /.docker/deploy/build/composer.sh && \
    sh /.docker/deploy/build/nodejs.sh && \
    apt-get -y autoclean


# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


CMD \
    sh /.docker/deploy/init/entrypoint.sh && \
    sh /.docker/deploy/init/daemon.sh