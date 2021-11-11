# Builds a Docker image for mesh generation,
# with gmsh and FreeCAD preinstalled.
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

# Use meshdb-desktop as base image
FROM unifem/meshdb-desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install gmsh and freecad
RUN add-apt-repository ppa:nschloe/gmsh-backports && \
    add-apt-repository ppa:freecad-maintainers/freecad-stable && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        gmsh \
        freecad && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

ADD image/home $DOCKER_HOME

########################################################
# Customization for user
########################################################

USER $DOCKER_USER
WORKDIR $DOCKER_HOME
USER root
