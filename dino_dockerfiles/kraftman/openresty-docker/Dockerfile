#
# Openresty docker image
#
# This docker contains openresty (nginx) compiled from source with useful optional modules installed.
#
# http://github.com/tenstartups/openresty-docker
#

FROM debian:jessie

MAINTAINER Marc Lennox <marc.lennox@gmail.com>

# Set environment.
ENV \
  DEBIAN_FRONTEND=noninteractive \
  TERM=xterm-color

# Install packages.
RUN apt-get update && apt-get -y install \
  build-essential \
  curl \
  libreadline-dev \
  libncurses5-dev \
  libpcre3-dev \
  libssl-dev \
  nano \
  perl \
  wget

# Compile openresty from source.
RUN \
  wget https://openresty.org/download/openresty-1.9.7.4.tar.gz && \
  tar -xzvf openresty-*.tar.gz && \
  rm -f openresty-*.tar.gz && \
  cd openresty-* && \
  ./configure --with-pcre-jit --with-ipv6 && \
  make && \
  make install && \
  make clean && \
  cd .. && \
  rm -rf openresty-*&& \
  ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx && \
  ldconfig

# Set the working directory.
WORKDIR /opt/openresty/

# Add files to the container.
COPY entrypoint /opt/
COPY nginx.example.conf /opt/

# Expose volumes.
VOLUME ["/opt/openresty"]

# Set the entrypoint script.
ENTRYPOINT ["/opt/entrypoint"]

# Define the default command.
CMD ["nginx", "-c", "/opt/openresty/conf/nginx.conf", "-p", "/opt/openresty"]
