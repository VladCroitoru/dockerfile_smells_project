FROM debian:jessie

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Set environment variables
ENV appDir /var/www/app/current

# Run updates and install deps
RUN apt-get update

# Install needed deps and clean up after
RUN apt-get install -y -q --no-install-recommends \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    g++ \
    gcc \
    git \
    make \
    nginx \
    sudo \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoclean

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 6.10.3

# Install nvm with node and npm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash \
&& source $NVM_DIR/nvm.sh \
&& nvm install $NODE_VERSION \
&& nvm alias default $NODE_VERSION \
&& nvm use default

# Set up our PATH correctly so we don't have to long-reference npm, node, &c.
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Set the work directory
RUN mkdir -p /var/www/app/current
WORKDIR ${appDir}

# Add our package.json and install *before* adding our application files
ADD package.json ./
RUN npm i --production

# Install pm2 *globally* so we can run our application
RUN npm i -g pm2

# Add application files
ADD . /var/www/app/current

#Expose the port
EXPOSE 8001

CMD ["pm2", "start", "processes.json", "--no-daemon"]
# the --no-daemon is a minor workaround to prevent the docker container from thinking pm2 has stopped running and ending itself