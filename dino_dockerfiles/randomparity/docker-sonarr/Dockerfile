FROM randomparity/docker-supervisor:latest
MAINTAINER David Christensen <randomparity@gmail.com>

ENV SONARR_LAST_UPDATE 2015-11-15

# Add the Sonarr repository and install the application
RUN DEBIAN_FRONTEND=noninteractive apt-key adv \
    --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \
    echo "deb http://apt.sonarr.tv/ master main" | \
    sudo tee /etc/apt/sources.list.d/sonarr.list && \
    DEBIAN_FRONTEND=noninteractive apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install nzbdrone

# We've got everything we need so clear out the apt data
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*

VOLUME ["/config", "/download", "/media"]

EXPOSE 8989

# Copy the supervisord configuration files into the container
COPY sonarr.conf /etc/supervisor/conf.d/sonarr.conf
RUN echo "user=$BASE_USER" >> /etc/supervisor/conf.d/sonarr.conf

# No need to setup a CMD directive since that was handled in the FROM image.
