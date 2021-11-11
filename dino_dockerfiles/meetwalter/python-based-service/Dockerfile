FROM phusion/baseimage:0.9.19
MAINTAINER Michael Williams
ENV REFRESHED_AT 2016-07-21

# Set correct environment variables.
ENV PYTHON_MAJOR 3.5
ENV PYTHON_VERSION 3.5.2

# ENV HOME does not seem to work currently; HOME is unset in Docker container.
# See discussion at: https://github.com/phusion/baseimage-docker/issues/119
RUN echo /root > /etc/container_environment/HOME

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Baseimage-docker enables an SSH server by default, so that you can use SSH
# to administer your container. In case you do not want to enable SSH, here's
# how you can disable it. Uncomment the following:
# RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use phusion/baseimage's init system.
CMD ["/sbin/my_init"]

# Set the locale.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# See discussion at: https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Remove traces of Debian Python.
RUN apt-get purge -y python.*

# Install dependencies and useful tools.
RUN apt-get update \
  && apt-get install -y ca-certificates netbase net-tools bzip2 mime-support \
  autoconf autotools-dev build-essential quilt gcc-multilib g++-multilib bison \
  dpkg-dev tk-dev tcl-dev blt-dev libgpm2 libtinfo-dev libncurses-dev \
  libncurses5-dev libncursesw5-dev libreadline-dev libreadline6-dev \
  zlib1g-dev libbz2-dev liblzma-dev libssl-dev libexpat1-dev libxml2-dev \
  libxslt1-dev libyaml-dev libffi6 libffi-dev libffi6-dbg libgdbm3 libgdbm-dev \
  libsqlite3-dev

# Build and install Python.
RUN mkdir -p /usr/src/python \
  && curl -SL "https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz" | tar -xz -f - -C /usr/src/python --strip-components=1 \
  && cd /usr/src/python \
  && ./configure --enable-ipv6 \
  && make -j"$(nproc)" \
  && make install \
  && rm -r /usr/src/python

# Make it the default Python.
RUN cd /usr/local/bin \
  && ln -sf easy_install-3.5 easy_install \
  && ln -sf idle3 idle \
  && ln -sf pydoc3 pydoc \
  && ln -sf python3 python \
  && ln -sf python3-config python-config

# Install Pip (and SetupTools).
RUN mkdir -p /usr/src/pip \
  && curl -o /usr/src/pip/get-pip.py https://bootstrap.pypa.io/get-pip.py \
  && python3 /usr/src/pip/get-pip.py

# Clean up.
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
