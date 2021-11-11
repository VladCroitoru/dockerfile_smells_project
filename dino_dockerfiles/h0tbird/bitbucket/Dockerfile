#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM java:openjdk-8-jre
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV BITBUCKET_HOME="/var/atlassian/application-data/bitbucket" \
    BITBUCKET_INSTALL_DIR="/opt/atlassian/bitbucket" \
    BITBUCKET_VERSION="4.5.2"

ENV DOWNLOAD_URL="https://downloads.atlassian.com/software/stash/downloads/atlassian-bitbucket-${BITBUCKET_VERSION}.tar.gz"

#------------------------------------------------------------------------------
# Update the base image:
#------------------------------------------------------------------------------

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends git libtcnative-1 \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

#------------------------------------------------------------------------------
# Install Bitbucket:
#------------------------------------------------------------------------------

RUN mkdir -p ${BITBUCKET_INSTALL_DIR} \
    && curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip=1 -C ${BITBUCKET_INSTALL_DIR} \
    && mkdir -p ${BITBUCKET_INSTALL_DIR}/conf/Catalina \
    && chmod -R 700 ${BITBUCKET_INSTALL_DIR}/conf/Catalina \
    && chmod -R 700 ${BITBUCKET_INSTALL_DIR}/logs \
    && chmod -R 700 ${BITBUCKET_INSTALL_DIR}/temp \
    && chmod -R 700 ${BITBUCKET_INSTALL_DIR}/work \
    && ln -s /usr/lib/x86_64-linux-gnu/libtcnative-1.so ${BITBUCKET_INSTALL_DIR}/lib/native/libtcnative-1.so

#------------------------------------------------------------------------------
# Populate root file system:
#------------------------------------------------------------------------------

ADD rootfs /

#------------------------------------------------------------------------------
# Expose stuff:
#------------------------------------------------------------------------------

EXPOSE 80
VOLUME ["${BITBUCKET_HOME}"]
WORKDIR ${BITBUCKET_INSTALL_DIR}
CMD ["./bin/start-bitbucket.sh", "-fg"]
