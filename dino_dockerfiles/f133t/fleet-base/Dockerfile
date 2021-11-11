
# docker build -t f133t/fleet-base:latest -f Dockerfile.base .

FROM ubuntu:16.04

RUN \
  apt-get update \
  && apt-get purge ruby \
  && apt-get install -y \
    sudo \
    netcat \
    mysql-client \
    libmysql++-dev \
    libsqlite3-dev \
    curl \
    build-essential \
    git \
    nodejs \
    nginx \
    libffi-dev \
    libssl-dev \
    libcrypto++-dev

RUN \
  useradd -d /home/ubuntu -m -s /bin/bash ubuntu \
  && echo "ubuntu:changeme" | chpasswd \
  && echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
  && sed -i s#/home/ubuntu:/bin/false#/home/ubuntu:/bin/bash# /etc/passwd

# Install the version of ruby we want:
RUN \
  apt-get install -y wget \
  && cd /tmp && \
  wget -O ruby-install-0.6.0.tar.gz \
    https://github.com/postmodern/ruby-install/archive/v0.6.0.tar.gz && \
  tar -xzvf ruby-install-0.6.0.tar.gz && \
  cd ruby-install-0.6.0/ && \
  sudo make install && \
  sudo ruby-install ruby 2.4.1 --system -- --disable-install-rdoc && \
  sudo ln -s /usr/local/ruby-2.4.1/bin/ruby /usr/bin/ruby && \
  sudo ln -s /usr/local/ruby-2.4.1/bin/gem /usr/bin/gem && \
  sudo ln -s /usr/local/ruby-2.4.1/bin/irb /usr/bin/irb

ENV PATH=/usr/local/ruby-2.4.1/bin:$PATH

USER ubuntu

RUN sudo gem install bundler --no-ri --no-rdoc \
  && sudo gem install foreman --no-ri --no-rdoc
