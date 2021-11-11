FROM jupyter/minimal-notebook:latest

MAINTAINER Maximilian Fellner <max.fellner@gmail.com>

# Install ijavascript dependencies. See https://github.com/n-riesco/ijavascript
USER root
ENV DEBIAN_FRONTEND noninteractive
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libzmq3-dev \
    && apt-get clean -y \
    && apt-get autoremove -y \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

USER root
ENV NODE_VERSION 6.0.0
ENV NODE_PACKAGE node-v$NODE_VERSION-linux-x64
RUN mkdir -p $HOME/.node-gyp
RUN wget -q https://nodejs.org/dist/v${NODE_VERSION}/${NODE_PACKAGE}.tar.xz \
    && tar xf ${NODE_PACKAGE}.tar.xz \
    && cp -R ${NODE_PACKAGE}/bin/* /usr/local/bin \
    && cp -R ${NODE_PACKAGE}/include/* /usr/local/include \
    && cp -R ${NODE_PACKAGE}/lib/* /usr/local/lib \
    && cp -R ${NODE_PACKAGE}/share/* /usr/local/share \
    && rm -r ${NODE_PACKAGE} \
    && rm ${NODE_PACKAGE}.tar.xz

# Install ijavascript as user jovyan
USER jovyan
ENV NODE_PATH /home/${NB_USER}/node_modules
ENV PATH ${NODE_PATH}/.bin:${PATH}
RUN npm install --prefix /home/$NB_USER ijavascript

# Modify startup script to run ijavascript
USER root
RUN printf "#!/bin/bash\n$(which ijs)\n" \
    > /usr/local/bin/start-notebook.sh

# Switch back to jovyan to avoid accidental container runs as root
USER jovyan
