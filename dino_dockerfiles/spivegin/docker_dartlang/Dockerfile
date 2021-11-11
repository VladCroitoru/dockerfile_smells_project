#
# ActiveFlyers Dartlang base

# Pull base image.
FROM bitnami/minideb:stretch

# Install Dart.
RUN install_packages curl
RUN \
  mkdir -p /tmp/dart && \
  cd /tmp/dart && \
  curl -O http://storage.googleapis.com/dart-archive/channels/stable/release/latest/linux_packages/dart_1.24.2-1_amd64.deb && \
  dpkg -i dart_1.24.2-1_amd64.deb && \
  rm -fr /tmp/dart

# Set environment variables.
ENV PATH /usr/lib/dart/bin:$PATH
RUN mkdir /opt/dart && mkdir /opt/dart/code && mkdir /opt/dart/data
# Define working directory.
WORKDIR /opt/dart/code

# Define default command.
CMD ["bash"]