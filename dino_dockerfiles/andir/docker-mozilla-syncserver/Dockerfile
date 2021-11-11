FROM debian:jessie

MAINTAINER Jonathan Dray <jonathan.dray@gmail.com>, BirgerK <birger.kamp@gmail.com>

# Configure APT
ENV DEBIAN_FRONTEND noninteractive
ENV SERVER_HOME /usr/local/share/syncserver
ENV CONFIG_HOME /usr/local/share/config
ENV DOCKERIZE_VERSION v0.2.0
ENV SERVER_VERSION master

# Base setup
# ADD resources/etc/apt/ /etc/apt/
RUN apt-get -y update && \
    apt-get install -q -y python2.7 python2.7-dev python-virtualenv make g++ git-core curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install dockerize
RUN curl -L -O https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    rm -rf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Get the latest version at https://github.com/mozilla-services/syncserver and run the build command
RUN cd /usr/local/share && \
    git clone https://github.com/mozilla-services/syncserver

WORKDIR $SERVER_HOME
RUN git checkout $SERVER_VERSION && \
    make build && \
    ./local/bin/pip install PyMySQL

# Add the configuration file
RUN mkdir $CONFIG_HOME
ADD resources/syncserver.ini.j2 $CONFIG_HOME/syncserver.ini.j2
ADD resources/entrypoint.sh /entrypoint.sh
RUN chmod +x /*.sh

# Run the Sync server
EXPOSE 5000
VOLUME [ "$CONFIG_HOME" ]
ENTRYPOINT ["/entrypoint.sh"]
