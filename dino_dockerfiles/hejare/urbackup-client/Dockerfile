FROM ubuntu:18.04

LABEL maintainer="henrik@hejare.se"

# Install the UrBackup client
WORKDIR /tmp/install
ADD urbackupclient_install_2.4.9.sh /tmp/install
RUN sh urbackupclient_install_2.4.9.sh silent
RUN rm -rf /tmp/install

# Make ports available to the world outside this container
EXPOSE 35621/TCP 35622/UDP 35623/TCP

# Add a healthcheck on the UrBackup client service
HEALTHCHECK CMD /etc/init.d/urbackupclientbackend status

# Start the UrBackup client service through the startup script
ADD urbackupclient_start.sh /usr/local/bin/urbackupclient_start.sh
CMD ["sh", "/usr/local/bin/urbackupclient_start.sh"]