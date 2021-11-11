FROM ubuntu

# install apache, postgres, and some basics
RUN apt-get update && apt-get install -yq \
    apache2 \
    build-essential \
    curl \
    git \
    libssl-dev \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    postgresql-client \
    psmisc \
    python \
    sudo \
    vim

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install nodejs using nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.9.1

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH

# configure postgres
RUN mkdir /data \
    && chown postgres /data \
    && sudo -u postgres /usr/lib/postgresql/9.5/bin/initdb /data

# this will be useful when bash is run interactively (can't use .bashrc in build steps unfortunately)
RUN echo ". \"$NVM_DIR/nvm.sh\" && sudo -u postgres /usr/lib/postgresql/9.5/bin/pg_ctl -D /data -l /data/logfile start && /etc/init.d/apache2 start" >> ~/.bashrc

# this is used by five-bells-service-manager to connect to postgres:
ENV USER postgres

# this is needed for https://github.com/interledgerjs/five-bells-integration-test/blob/2e76852/src/tests/ilp-kit.js#L33:
ENV CIRCLE_BUILD_IMAGE ubuntu-14.04

# now add this repo and run all the steps necessary to get ready for the test-running itself:
ADD . /app
WORKDIR /app
RUN source $NVM_DIR/nvm.sh && npm install

# at this point, the circle.yml from this repo specifies to
# simply run `npm run integration`, which does two things:
# 1. integration-loader
# 2. node ./src/bin/integration all
# but this second step is equivalent to:
#   2a. node ./src/bin/integration setup
#   2b. node ./src/bin/integration test
# In the build phase we're doing 1. and 2a.:
RUN source $NVM_DIR/nvm.sh && ./node_modules/.bin/integration-loader
RUN source $NVM_DIR/nvm.sh && node ./src/bin/integration setup

# the following is necessary, because:
# https://github.com/interledgerjs/five-bells-integration-test-loader/blob/4c6f4da/src/lib/dependency-manager.js#L133
# should have triggered:
# https://github.com/interledgerjs/ilp-kit/blob/41986c5/package.json#L29
# but because the build steps run as root, that postinstall hook fails with an error as described here:
# http://stackoverflow.com/questions/18136746/npm-install-failed-with-cannot-run-in-wd
# (skipping the `npm rebuild node-sass` part since webpack seems to work fine now, without it)
RUN source $NVM_DIR/nvm.sh && cd integration-test/ilp-kit && npm run build

# and we leave 2b. from `npm run integration` as the run-time command:
CMD source ~/.bashrc && ./src/bin/integration test

# to use this Dockerfile, simply do something like:
# docker build -t five-bells-integration-test .
# docker run -it five-bells-integration-test /bin/bash
# $ ls
# $ src/bin/integration test basic connector_first
# $ src/bin/integration test
# $ exit
# docker run five-bells-integration-test
