FROM tomcat:9.0

# Install necessary packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
    net-tools \
    exuberant-ctags \
    git-core \
    subversion \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install opengrok
RUN mkdir /opengrok && wget https://github.com/OpenGrok/OpenGrok/releases/download/1.1-rc5/opengrok-1.1-rc5.tar.gz && tar xf opengrok-1.1-rc5.tar.gz -C /opengrok --strip-components=1
RUN rm -f opengrok-1.1-rc5.tar.gz

# Deploy opengrok
ENV OPENGROK_INSTANCE_BASE /var/opengrok
ENV OPENGROK_TOMCAT_BASE=/usr/local/tomcat/
RUN mkdir -p ${OPENGROK_INSTANCE_BASE}/{etc,data} && /opengrok/bin/OpenGrok deploy
RUN mkdir /SRC_ROOT
ENV OPENGROK_SOURCE_DIR /SRC_ROOT

# Network setting
EXPOSE 8080
