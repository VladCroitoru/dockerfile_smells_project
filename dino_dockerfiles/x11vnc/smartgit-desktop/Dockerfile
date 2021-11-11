# Builds a Docker image with Ubuntu 17.10, g++-5.4, and Smartgit
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM x11vnc/desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

ARG SMARTGIT_VER=19.1.0
ADD image/home $DOCKER_HOME/

# Install Java
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
        git \
        openjdk-8-jre-headless && \
    apt-get clean && \
    echo "move_to_config smartgit" >> /usr/local/bin/init_vnc && \
    rm -rf /var/lib/apt/lists/*

# Install smartgit
RUN /bin/bash -c 'curl -L -O https://www.syntevo.com/downloads/smartgit/smartgit-${SMARTGIT_VER//\./_}.deb && \
    dpkg -i smartgit-${SMARTGIT_VER//\./_}.deb' && \
    echo "@/usr/share/smartgit/bin/smartgit.sh" >> /home/$DOCKER_USER/.config/lxsession/LXDE/autostart && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME && \
    rm -rf /tmp/* /var/tmp/*

WORKDIR $DOCKER_HOME
