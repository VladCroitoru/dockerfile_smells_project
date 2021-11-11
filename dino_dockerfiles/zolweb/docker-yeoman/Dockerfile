# Yeoman with some generators and prerequisites
FROM ubuntu:14.04

# Install node.js
RUN apt-get -yq update && \
    apt-get -yq install git curl net-tools sudo bzip2 libpng-dev

RUN curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get -yq install nodejs

# Install npm, yeoman and generators
RUN npm install -g npm@latest && \
    npm install -g yo bower grunt-cli && \
    npm install -g generator-webapp generator-angular

# Install Ruby & Compass
RUN apt-get -yq install ruby && \
    apt-get build-dep -yq --force-yes ruby-compass && \
    gem install compass && \
    npm install -g grunt-contrib-compass

# Add a yeoman user because grunt doesn't like being root
ENV LANG en_US.UTF-8
RUN adduser --disabled-password --gecos "" yeoman && \
    echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV HOME /home/yeoman

WORKDIR /src

# Expose the port
EXPOSE 9000

# Always run as the yeoman user
USER yeoman