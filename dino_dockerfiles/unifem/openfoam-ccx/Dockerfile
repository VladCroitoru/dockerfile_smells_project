# Builds a Docker image for OpenFOAM and Calculix in a Desktop 
# environment with Ubuntu and LXDE.
#
# The built image can be found at:
#   https://hub.docker.com/r/unifem/openfoam-cxx
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use mapper-desktop as base image
FROM unifem/mapper-desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install OpenFOAM 5.0 (https://openfoam.org/download/5-0-ubuntu/), 
# Calculix, along with FreeCAD and Gmsh
RUN sh -c "curl -s http://dl.openfoam.org/gpg.key | apt-key add -" && \
    add-apt-repository http://dl.openfoam.org/ubuntu && \
    add-apt-repository ppa:freecad-maintainers/freecad-stable && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        openfoam5 \
        paraviewopenfoam54 \
	freecad \
        calculix-ccx \
        gmsh && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER $DOCKER_USER
WORKDIR $DOCKER_HOME

# Source configuration for bash
# https://github.com/OpenFOAM/OpenFOAM-dev/tree/version-5.0/etc
RUN echo "source /opt/openfoam5/etc/bashrc" >> $DOCKER_HOME/.profile

USER root
