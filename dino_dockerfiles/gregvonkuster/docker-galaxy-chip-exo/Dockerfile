# Galaxy - ChIP-exo flavor
#
# VERSION       0.1

FROM quay.io/bgruening/galaxy:18.01

MAINTAINER Greg Von Kuster, ghv2@psu.edu

ENV GALAXY_CONFIG_BRAND="Galaxy ChIP-exo"

# Install ChIP-exo tools
ADD chipexo_tools.yml $GALAXY_ROOT/tools.yaml
RUN install-tools $GALAXY_ROOT/tools.yaml && \
    /tool_deps/_conda/bin/conda clean --tarballs
