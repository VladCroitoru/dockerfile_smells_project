FROM debian:8

LABEL r2docker 1.3.0

# Radare version
ENV R2_VERSION 1.3.0
# R2pipe python version
ENV R2_PIPE_PY_VERSION 0.8.9
# R2pipe node version
ENV R2_PIPE_NPM_VERSION 2.3.2

# Build radare2 in a volume to minimize space used by build
VOLUME ["/src"]
# Install docker in only one layer to minimize space
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
     apt-get install -y \
     curl \
     gcc \
     git \
     bison \
     pkg-config \
     make \
     glib-2.0 \
     sudo && \
     curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
     apt-get install -y nodejs python-pip && \
     curl -sL https://www.npmjs.com/install.sh | bash - && \
     pip install r2pipe=="$R2_PIPE_PY_VERSION" && \
     npm install -g "r2pipe@$R2_PIPE_NPM_VERSION" && \
     cd /src && \
     git clone -b "$R2_VERSION" --depth 1 https://github.com/radare/radare2.git && \
     cd radare2 && \
     ./sys/install.sh && \
     make install && \
     apt-get remove --purge -y \
     curl \
     gcc \
     git \
     bison \
     pkg-config \
     make \
     python-pip \
     glib-2.0 && \
     apt-get autoremove --purge -y && \
     apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /src
ENV HOME /src

CMD ["/bin/bash"]
