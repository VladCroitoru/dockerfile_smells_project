# Make Debian base image a variable (default value added for automated build on hub)
ARG   DEBIAN_VERSION=stretch-slim

FROM  debian:${DEBIAN_VERSION}
MAINTAINER Olivier Orabona <olivier.orabona@gmail.com>

# This has to be after FROM directive since it comes after pulling image
ARG   INSTALL_METEOR=true
ARG   METEOR_VERSION=latest
ARG   INSTALL_MONGO=false
ARG   INSTALL_NGINX=false
ARG   EXTRA_PREINSTALL_SCRIPT
ARG   EXTRA_POSTINSTALL_SCRIPT

# Global environment for everything following
ENV DEBIAN_FRONTEND noninteractive

# Default values for Meteor environment variables
ENV ROOT_URL=http://localhost \
    MONGO_URL=mongodb://127.0.0.1:27017/meteor \
    MAIL_URL=smtp://xxx:yyy@zzz.tld \
    PORT=3000 \
    METEOR_SETTINGS_FILE=settings.json \
    MONGO_OPLOG_URL=mongodb://mongodb/local \
    APP_MAINJS=main.js

# Expose both but only one should be used after deployment
EXPOSE 3000/tcp 80/tcp

# build directories
ENV APP_SOURCE_DIR=/usr/src/app \
    APP_BUNDLE_DIR=/home/meteor/ \
    BUILD_SCRIPTS_DIR=/opt/build_scripts \
    TOOL_NODE_FLAGS=$TOOL_NODE_FLAGS

# Add entrypoint and other build scripts and (optional) conf files
COPY scripts conf $BUILD_SCRIPTS_DIR/

# We need to make sure scripts can be run without requiring root.
# Also, build.sh here is needed to build "base" image(s).
RUN chmod -R 755 $BUILD_SCRIPTS_DIR && sync && \
  $BUILD_SCRIPTS_DIR/build.sh

# copy the app to the container
ONBUILD COPY . $APP_SOURCE_DIR

# Alter image with new software if needed then build app, finish with clean up
ONBUILD RUN   $BUILD_SCRIPTS_DIR/build.sh && \
  $BUILD_SCRIPTS_DIR/build-project.sh && \
  $BUILD_SCRIPTS_DIR/post-build-cleanup.sh

WORKDIR $BUILD_SCRIPTS_DIR

# start the app
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["start"]
