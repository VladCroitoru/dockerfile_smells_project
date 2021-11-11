FROM combro2k/debian-debootstrap:8

MAINTAINER Martijn van Maurik <docker@vmaurik.nl>

# Environment variables
ENV HOME=/root \
    INSTALL_LOG=/var/log/build.log

# Add first the scripts to the container
ADD resources/bin/ /usr/local/bin/

# Run the installer script
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh build'

# Run the last bits and clean up
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh post_install' | tee -a ${INSTALL_LOG} > /dev/null 2>&1 || exit 1

EXPOSE 9987/udp 10011/tcp 30033/tcp

# Inject a Volume for any TS3-Data that needs to be persisted or to be accessible from the host. (e.g. for Backups)
VOLUME ["/teamspeak3"]

CMD ["/usr/local/bin/run"]
