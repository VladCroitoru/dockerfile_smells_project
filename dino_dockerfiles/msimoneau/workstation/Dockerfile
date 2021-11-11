# Ubuntu workstation.

FROM ubuntu:16.04

MAINTAINER Martin Simoneau "martin1.simoneau@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# Set Timezone
RUN echo "America/Montreal" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

## Set LOCALE to UTF8
RUN apt-get install -y locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8

# Install utils.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y openssh-server && \
    apt-get install -y git build-essential && \
    apt-get install -y openssl libssl-dev && \
    apt-get install -y wget curl tcpdump zip unzip libfontconfig1-dev python && \
    apt-get autoclean

# Install Ruby 2.3 and sass
RUN apt-get install -y software-properties-common && \
    apt-add-repository ppa:brightbox/ruby-ng && \
    apt-get update && \
    apt-get install -y ruby2.3 && \
    gem install sass

# Install nodejs 4.6 (https://nodejs.org/en/download/package-manager/)
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - &&\
    apt-get install -y nodejs &&\
    update-alternatives --install "/usr/bin/node" "node" "/usr/bin/nodejs" 1

# Bower and grunt and aungular-cli
RUN npm install -g bower && \
    npm install -g grunt && \
    npm install -g gulp-cli && \
    npm install -g @angular/cli

# Add a user.
ARG user=admin
RUN adduser --disabled-password --gecos '' ${user} && \
    adduser ${user} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
    usermod -s /bin/bash ${user}

ENV HOME /home/${user}
WORKDIR ${HOME}
VOLUME ["${HOME}"]

USER ${user}
