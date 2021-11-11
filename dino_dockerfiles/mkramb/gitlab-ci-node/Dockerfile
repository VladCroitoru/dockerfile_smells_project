FROM ubuntu

ENV NVM_DIR /usr/local/nvm
ENV NVM_NODE_VERSION 6.5.0
ENV PATH $NVM_DIR/versions/node/v$NVM_NODE_VERSION/bin:$PATH

# make sure apt is up to date
RUN apt-get update --fix-missing
RUN apt-get install -y bash wget git libpng12-0 libelf1

# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install nvm with node and npm
RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install $NVM_NODE_VERSION \
    && nvm alias default $NVM_NODE_VERSION \
    && nvm use default
