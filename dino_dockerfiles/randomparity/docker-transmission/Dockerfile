FROM randomparity/docker-supervisor:latest
MAINTAINER David Christensen <randomparity@gmail.com>

ENV TRANSMISSION_LAST_UPDATE 2015-07-23

# Add the Transmission repository and install the transmission application
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:transmissionbt/ppa && \
    DEBIAN_FRONTEND=noninteractive apt-get -q update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install transmission-daemon

# Clean-up any unneeded files
RUN DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/* && \
    rm -rf /tmp/*

VOLUME ["/config", "/download"]

# Used by transmission daemon to set default configuration data location
ENV TRANSMISSION_HOME /config

EXPOSE 9091 51413

# Copy the supervisord configuration files into the container
COPY transmission.conf /etc/supervisor/conf.d/transmission.conf
RUN echo "user=$BASE_USER" >> /etc/supervisor/conf.d/transmission.conf
COPY cron.conf /etc/supervisor/conf.d/cron.conf

# Copy the torrent scan script into the container and make it executable
COPY torrent-scan.sh /bin/torrent-scan.sh
RUN chmod +x /bin/torrent-scan.sh

# Copy and install the torrent scanning crontab entry
COPY torrent-crontab /root/torrent-crontab
RUN /usr/bin/crontab /root/torrent-crontab

# No need to setup a CMD directive since that was handled in the FROM image.
