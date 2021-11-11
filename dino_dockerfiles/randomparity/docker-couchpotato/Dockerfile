FROM randomparity/docker-supervisor:latest
MAINTAINER David Christensen <randomparity@gmail.com>

ENV COUCHPOTATO_LAST_UPDATE 2015-09-04

# Install prerequisites
RUN DEBIAN_FRONTEND=noninteractive apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install \
    unrar

# Clean-up any unneeded files
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*

# Fetch the Couchpotato package (select a known release rather than a git clone)
RUN mkdir -p /opt/couchpotato && \
    wget -qO - https://github.com/RuudBurger/CouchPotatoServer/archive/build/3.0.1.tar.gz | \
    tar -C /opt/couchpotato -zx --strip-components 1 && \
    chown -R $BASE_USER:$BASE_GROUP /opt/couchpotato

VOLUME ["/config", "/download", "/media"]

EXPOSE 5050

# Copy the supervisord configuration files into the container
COPY couchpotato.conf /etc/supervisor/conf.d/couchpotato.conf
RUN echo "user=$BASE_USER" >> /etc/supervisor/conf.d/couchpotato.conf

# No need to setup a CMD directive since that was handled by FROM image.
