FROM ubuntu:16.04
LABEL maintainer="Jonathan Hanson (jonathan@jonathan-hanson.org)"

ENV znc_version=1.6.6
ARG znc_clientbuffer_gitref=7ae14f82f74eee552d0bfdd9e6c6e96a2b31608d
ENV znc_exec_user=znc-admin
ARG znc_user_group_id=1066
ENV znc_config_root=/etc/znc
ARG znc_port=6666

RUN apt-get update && apt-get install -y \
      build-essential \
      curl \
      libicu-dev \
      libperl-dev \
      libssl-dev \
      pkg-config \
      swig3.0 \
    && rm -rf /var/lib/apt/lists/*

# Fetch build sources, and unpack the source into the source directory
# This includes the ClientBuffer module source file
ADD http://znc.in/releases/archive/znc-$znc_version.tar.gz /tmp/
RUN tar -xvf /tmp/znc-$znc_version.tar.gz -C /usr/local/src
ADD https://raw.githubusercontent.com/CyberShadow/znc-clientbuffer/$znc_clientbuffer_gitref/clientbuffer.cpp /usr/local/src/znc-$znc_version/modules/
RUN rm -rf /tmp/znc-$znc_version.tar.gz

# Make and install ZNC
WORKDIR /usr/local/src/znc-$znc_version
RUN ./configure \
    && make \
    && make install

# Set up the ZNC user and group
RUN groupadd -r --gid $znc_user_group_id $znc_exec_user \
    && useradd --no-log-init -r --uid $znc_user_group_id -g $znc_exec_user $znc_exec_user

# Set up the ZNC self signed certificate
RUN mkdir -p $znc_config_root && chown $znc_exec_user:$znc_exec_user $znc_config_root

# Set up the ZNC configuration directory
VOLUME $znc_config_root

# set up the service to run when the container starts
USER $znc_exec_user
EXPOSE $znc_port

# When the container starts, generate a `znc.pem` file in the config directory,
# if it doesn't already exist.  Then run whatever CMD passes.
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

#CMD /usr/local/bin/znc --datadir=$znc_config_root --foreground --debug
CMD /usr/local/bin/znc --datadir=$znc_config_root --foreground
