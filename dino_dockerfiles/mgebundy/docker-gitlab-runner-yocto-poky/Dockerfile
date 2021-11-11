FROM ubuntu:14.04

MAINTAINER Mitchell Bundy <mitch@bundy.ca>

RUN apt update \
  && apt upgrade -y \
	&& apt install -y --no-install-recommends \
  gawk \
  wget \
  git \
  diffstat \
  unzip \
  texinfo \
  gcc-multilib \
  build-essential \
  chrpath \
  socat \
  cpio \
  python \
  python3 \
  python3-pip \
  python3-pexpect \
  xz-utils \
  debianutils \
  iputils-ping \
  libsdl1.2-dev \
  xterm \
  locales \
  openssh-client \
	&& rm -rf /var/lib/apt/lists/*

# Fix error "Please use a locale setting which supports utf-8."
# See https://wiki.yoctoproject.org/wiki/TipsAndTricks/ResolvingLocaleIssues
RUN dpkg-reconfigure locales \
  && locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Create a non-root user that will perform the actual build
RUN id build 2>/dev/null || useradd --uid 30000 --create-home build
RUN echo "build ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers

USER build
WORKDIR /home/build

RUN git clone -b pyro git://git.yoctoproject.org/poky
