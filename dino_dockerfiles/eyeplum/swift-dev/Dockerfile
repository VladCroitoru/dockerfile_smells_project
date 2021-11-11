FROM ubuntu:16.04
MAINTAINER Yan Li<eyeplum@gmail.com>

# Latest Swift Version
ENV SWIFT_BRANCH development
ENV SWIFT_VERSION swift-DEVELOPMENT-SNAPSHOT-2017-12-30-a
ENV SWIFT_PLATFORM ubuntu16.04

# Install Dependencies
RUN apt-get update && \
    apt-get install -y \
        clang \
        cmake \
        libedit2 \
        libxml2 \
        libicu55 \
        libpython2.7 \
        ninja-build \
        wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Swift keys
RUN wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - && \
    gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift

# Download and install Swift
RUN SWIFT_ARCHIVE_NAME=$SWIFT_VERSION-$SWIFT_PLATFORM && \
    SWIFT_URL=https://swift.org/builds/$SWIFT_BRANCH/$(echo "$SWIFT_PLATFORM" | tr -d .)/$SWIFT_VERSION/$SWIFT_ARCHIVE_NAME.tar.gz && \
    wget $SWIFT_URL && \
    wget $SWIFT_URL.sig && \
    gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \
    tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz -C / --strip 1 && \
    rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*

