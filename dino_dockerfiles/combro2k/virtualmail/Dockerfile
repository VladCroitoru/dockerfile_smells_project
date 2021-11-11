FROM combro2k/debian-debootstrap:8

MAINTAINER Martijn van Maurik <docker@vmaurik.nl>

# Environment variables
ENV HOME=/root \
    INSTALL_LOG=/var/log/build.log \
    AMAVISD_DB_HOME=/var/lib/amavis/db

# Add resources
ADD resources/bin/ /usr/local/bin/

RUN chmod +x /usr/local/bin/* && touch ${INSTALL_LOG} && /bin/bash -l -c '/usr/local/bin/setup.sh build'

# Add remaining resources
ADD resources/etc/ /etc/
ADD resources/opt/ /opt/

# Run the last bits and clean up
RUN /bin/bash -l -c '/usr/local/bin/setup.sh post_install | tee -a ${INSTALL_LOG} > /dev/null 2>&1'

EXPOSE 25 80 110 143 465 587 993 995 4190

VOLUME ["/etc/skeletons", "/var/vmail", "/var/mailman", "/data/ssl"]

CMD ["/usr/local/bin/run"]

