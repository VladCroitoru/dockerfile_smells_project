# Galaxy Constructive Solid Geometry flavor

FROM bgruening/galaxy-stable:19.01

MAINTAINER Greg Von Kuster, ghv2@psu.edu

RUN apt-get -qq update && apt-get install --no-install-recommends -y libgl1-mesa-dev libgl1-mesa-dri libglu1-mesa x11-xserver-utils x11vnc xinit xserver-xorg-video-dummy xserver-xorg-input-void

ENV GALAXY_CONFIG_BRAND="Galaxy CSG"

# Install CSG tools
ADD csg.yaml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs
