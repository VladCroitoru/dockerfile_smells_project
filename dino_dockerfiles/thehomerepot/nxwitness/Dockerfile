FROM lsiobase/ubuntu:bionic
MAINTAINER Ryan Flagler

# global environment settings
ENV DEBIAN_FRONTEND="noninteractive"
ENV COMPANY_NAME="networkoptix"
ENV SOFTWARE_URL="https://updates.networkoptix.com/default/4.2.0.33117/linux/nxwitness-server-4.2.0.33117-linux64-patch.deb"

# pull installer
RUN     mkdir -p /opt/deb && \
        curl -o /opt/deb/${COMPANY_NAME}.deb -L "${SOFTWARE_URL}"
        
# modify user
RUN     usermod -l $COMPANY_NAME abc && \
        groupmod -n $COMPANY_NAME abc && \
        sed -i "s/abc/\$COMPANY_NAME/g" /etc/cont-init.d/10-adduser

# install packages
RUN     apt-get update && \
        apt-get install --no-install-recommends --yes \
                gdb \
                /opt/deb/${COMPANY_NAME}.deb && \
        apt-get clean && \
        apt-get autoremove --purge && \
        rm -rf \
                /opt/deb \
                /tmp/* \
                /var/lib/apt/lists/* \
                /var/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 7001
VOLUME /config /archive
