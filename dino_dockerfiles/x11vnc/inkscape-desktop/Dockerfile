# Builds a Docker image with Ubuntu 16.04 and Inkscape
#
# Authors:
# Xiangmin Jiao <xmjiao@gmail.com>

FROM x11vnc/desktop:latest
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"

USER root
WORKDIR /tmp

# Install texlive and inkscape
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
        texlive-generic-recommended \
        texlive-fonts-recommended \
        texlive-latex-base \
        python-lxml \
        pstoedit \
        inkscape  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER $DOCKER_USER
RUN echo '@inkscape' >> $DOCKER_HOME/.config/lxsession/LXDE/autostart

USER root

WORKDIR $DOCKER_HOME
