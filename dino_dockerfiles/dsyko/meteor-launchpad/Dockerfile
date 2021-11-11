FROM ubuntu:18.04
MAINTAINER David Sykora <dsykora@gmail.com>

RUN groupadd -r node && useradd -m -g node node

# Gosu
ENV GOSU_VERSION 1.13

#Maybe fix an issue with MongoDB version 4.2 asking for user input on install, from: https://github.com/phusion/baseimage-docker/issues/58
ENV DEBIAN_FRONTEND noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

#Java Runtime, used by open office
# RUN \
#   apt-get update && \
#   apt-get install -y openjdk-8-jre && \
#   rm -rf /var/lib/apt/lists/*


# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# MongoDB
ENV MONGO_VERSION 4.2.14
ENV MONGO_MAJOR 4.2
ENV MONGO_PACKAGE mongodb-org

# PhantomJS
ENV PHANTOM_VERSION 2.1.1

# build directories
ENV APP_SOURCE_DIR /opt/meteor/src
ENV APP_BUNDLE_DIR /opt/meteor/dist
ENV BUILD_SCRIPTS_DIR /opt/build_scripts
ENV BUILD_DIR /usr/local/share
ENV CACHE_DIR /tmp

# Add entrypoint and build scripts
COPY scripts $BUILD_SCRIPTS_DIR
RUN chmod -R 750 $BUILD_SCRIPTS_DIR

# Define all --build-arg options
ONBUILD ARG APT_GET_INSTALL
ONBUILD ENV APT_GET_INSTALL $APT_GET_INSTALL

ONBUILD ARG NODE_VERSION
ONBUILD ENV NODE_VERSION ${NODE_VERSION:-8.11.4}

ONBUILD ARG NPM_TOKEN
ONBUILD ENV NPM_TOKEN $NPM_TOKEN

ONBUILD ARG INSTALL_MONGO
ONBUILD ENV INSTALL_MONGO $INSTALL_MONGO

ONBUILD ARG INSTALL_MONGO_TOOLS
ONBUILD ENV INSTALL_MONGO_TOOLS $INSTALL_MONGO_TOOLS

ONBUILD ARG INSTALL_PHANTOMJS
ONBUILD ENV INSTALL_PHANTOMJS $INSTALL_PHANTOMJS

ONBUILD ARG INSTALL_GRAPHICSMAGICK
ONBUILD ENV INSTALL_GRAPHICSMAGICK $INSTALL_GRAPHICSMAGICK

# Node flags for the Meteor build tool
ONBUILD ARG TOOL_NODE_FLAGS
ONBUILD ENV TOOL_NODE_FLAGS "--max_old_space_size=4096"

ONBUILD ENV NODE_TLS_REJECT_UNAUTHORIZED "0"

#Set Memory Limit
ENV TOOL_NODE_FLAGS="--max_old_space_size=4096"

# optionally custom apt dependencies at app build time
ONBUILD RUN if [ "$APT_GET_INSTALL" ]; then apt-get update && apt-get install -y $APT_GET_INSTALL; fi

# copy the app to the container
ONBUILD COPY . $APP_SOURCE_DIR

# install all dependencies, build app, clean up
ONBUILD RUN cd $APP_SOURCE_DIR && \
  $BUILD_SCRIPTS_DIR/install-deps.sh && \
  $BUILD_SCRIPTS_DIR/install-node.sh && \
  $BUILD_SCRIPTS_DIR/install-phantom.sh && \
  $BUILD_SCRIPTS_DIR/install-graphicsmagick.sh && \
  $BUILD_SCRIPTS_DIR/install-ffmpeg.sh $BUILD_DIR $CACHE_DIR && \
  $BUILD_SCRIPTS_DIR/install-mediainfo.sh $BUILD_DIR $CACHE_DIR && \
  $BUILD_SCRIPTS_DIR/install-wkhtmltopdf.sh $BUILD_DIR $CACHE_DIR && \
  $BUILD_SCRIPTS_DIR/install-libreoffice.sh $BUILD_DIR $CACHE_DIR && \
  $BUILD_SCRIPTS_DIR/install-mongo.sh && \
  $BUILD_SCRIPTS_DIR/install-meteor.sh && \
  $BUILD_SCRIPTS_DIR/build-meteor.sh && \
  $BUILD_SCRIPTS_DIR/post-build-cleanup.sh

# Default values for Meteor environment variables
ENV PORT 3000

EXPOSE 3000

WORKDIR $APP_BUNDLE_DIR/bundle

# start the app
ENTRYPOINT ["./entrypoint.sh"]
CMD ["node", "main.js"]
