FROM combro2k/debian-debootstrap:8

MAINTAINER Martijn van Maurik <docker@vmaurik.nl>

# Environment variables
ENV HOME=/data \
    INSTALL_LOG=/var/log/build.log

# Add resources
ADD resources/bin /usr/local/bin/

# Run builder
RUN chmod +x /usr/local/bin/* && touch ${INSTALL_LOG} && /bin/bash -l -c '/usr/local/bin/setup.sh build'

# Add remaining resources
ADD resources/etc/ /etc/

# Run the last bits and clean up
RUN /bin/bash -l -c '/usr/local/bin/setup.sh post_install' | tee -a ${INSTALL_LOG} > /dev/null 2>&1

EXPOSE 80

# Decouple our data from our container.
VOLUME ["/data"]

CMD ["/usr/local/bin/run"]