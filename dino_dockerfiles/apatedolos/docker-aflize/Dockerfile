# Pull base image.
FROM ubuntu:14.04
# set non persistant noninteractive session
ARG DEBIAN_FRONTEND=noninteractive
# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update --quiet && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common python-software-properties && \
  apt-get install -y byobu curl git htop man unzip screen vim wget llvm libtool lcov && \
  add-apt-repository ppa:ubuntu-lxc/lxd-stable && \
  apt-get update && \
  apt-get install -y gcc g++ ca-certificates procps tar gzip make gdb golang clang bison automake libglib2.0-dev python-setuptools && \
  rm -rf /var/lib/apt/lists/*
  # Setup AFL Latest
RUN wget 'http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz' -O- | tar zxvf - && \
  cd afl-* && \
  PREFIX=/usr make install && \
  # Setup LLVM
  cd llvm_mode && \
  LLVM_CONFIG=llvm-config-3.4 make && \
  cd ../ && \
  PREFIX=/usr make install && \
  # Setup Qemu mode
  cd qemu_mode/ && ./build_qemu_support.sh && \
  cp /afl-*/afl-qemu-trace /usr/bin/

# Make sure afl-gcc will be run. This forces us to set AFL_CC and AFL_CXX or
# otherwise afl-gcc will be trying to call itself by calling gcc.
ADD ./afl-sh-profile /etc/profile.d/afl-sh-profile
RUN ln -s /etc/profile.d/afl-sh-profile /etc/profile.d/afl-sh-profile.sh

# It looks like /etc/profile.d isn't read for some reason, but .bashrc is.
# Let's include /etc/profile.d/afl-sh-profile from there.
RUN echo '. /etc/profile.d/afl-sh-profile' >> /root/.bashrc && chmod +x /root/.bashrc

RUN chmod +x /etc/profile.d/afl-sh-profile
ADD ./setup-afl_cc /usr/bin/setup-afl_cc
RUN chmod +x /usr/bin/setup-afl_cc && /usr/bin/setup-afl_cc

ADD ./afl-fuzz-parallel /usr/bin/

ADD ./install-preeny.sh /tmp/
RUN chmod +x /tmp/install-preeny.sh && /tmp/install-preeny.sh

RUN mkdir ~/pkg ~/pkgs ~/logs

# install "Crashwalk" set path to exploitable.py

ADD ./crashwalk.sh /tmp/
RUN chmod +x /tmp/crashwalk.sh && /tmp/crashwalk.sh

RUN mkdir ~/fuzz-results ~/pkgs-coverage
ADD ./scripts /afl-2.33b/scripts/
ADD ./fuzz-pkg-with-coverage.sh /root/
RUN chmod +x /root/fuzz-pkg-with-coverage.sh
ADD ./aflize /usr/bin/aflize
RUN chmod +x /usr/bin/aflize

# Add some of the settings I find it hard to live without.
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
RUN echo "syntax on" >> /root/.vimrc
