FROM randomparity/docker-supervisor:latest
MAINTAINER David Christensen <randomparity@gmail.com>

ENV SABNZBD_LAST_UPDATE 2015-01-27

# Add the Sabnzbd repository and install the application
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:jcfp/ppa && \
    DEBIAN_FRONTEND=noninteractive apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install \
    par2 unzip unrar sabnzbdplus sabnzbdplus-theme-classic \
    sabnzbdplus-theme-mobile sabnzbdplus-theme-plush \
    python-yenc

# We've got everything we need so clear out the apt data
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*

VOLUME ["/config", "/download"]

EXPOSE 8080

# Copy the supervisord configuration files into the container
COPY sabnzbd.conf /etc/supervisor/conf.d/sabnzbd.conf
RUN echo "user=$BASE_USER" >> /etc/supervisor/conf.d/sabnzbd.conf

# No need to setup a CMD directive since that was handled in the FROM container.
