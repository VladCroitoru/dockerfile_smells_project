# Pull base image
FROM buildpack-deps:latest

# Set default arguments
ARG FUSE_VERSION="2.9.7"
ARG FUSE_BUILD_DIR="/fuse-build"

# Set environment variables
ENV FUSE_VERSION=$FUSE_VERSION

# Copy startup script
COPY fuse-build.sh /tmp/fuse-build.sh

# Install build script
RUN install -o root -g root -m 0755 /tmp/fuse-build.sh /usr/local/bin \
        && rm -rf /tmp/*

# Define mountable directories
VOLUME $FUSE_BUILD_DIR

# Define working directory
WORKDIR $FUSE_BUILD_DIR

# Define default command
CMD ["fuse-build.sh"]
