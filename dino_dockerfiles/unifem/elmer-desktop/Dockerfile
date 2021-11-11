# Builds a Docker image for Elmer in a Desktop environment
# with Ubuntu and LXDE.
#
# The built image can be found at:
#   https://hub.docker.com/r/unifem/elmer-desktop
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM unifem/desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install Elmer and some additional tools (Gmsh, gfortran, etc.)
RUN apt-add-repository ppa:elmer-csc-ubuntu/elmer-csc-ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        gfortran \
        gmsh \
        elmerfem-csc && \
    echo "@ElmerGUI" >> $DOCKER_HOME/.config/lxsession/LXDE/autostar && \         
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

########################################################
# Customization for user and location
########################################################

WORKDIR $DOCKER_HOME

USER root
