FROM ubuntu:14.04

# Install node.js
RUN apt-get -yq update && \
    apt-get -yq install git curl net-tools sudo

RUN curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get -yq install nodejs

# Install npm, yeoman and generators
RUN npm install -g npm@latest && \
    npm install -g bower grunt-cli

# Install Ruby & Compass
RUN apt-get -yq install ruby && \
    apt-get build-dep -yq --force-yes ruby-compass && \
    gem install compass && \
    npm install -g grunt-contrib-compass

WORKDIR /src
