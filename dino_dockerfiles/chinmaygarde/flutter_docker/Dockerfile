# Flutter Engine Development
# ==========================
#
# docker run --cap-add=SYS_PTRACE --rm -it -v `pwd`:/WorkDir -w /WorkDir chinmaygarde/flutter_docker /bin/bash

FROM ubuntu:rolling
MAINTAINER Chinmay Garde, chinmaygarde@gmail.com

# Update dependencies.
RUN apt-get update

# Install dependencies.
RUN apt-get install -y         \
      autoconf                 \
      build-essential          \
      ccache                   \
      checkinstall             \
      cmake                    \
      curl                     \
      gdb                      \
      git                      \
      golang                   \
      libbz2-dev               \
      libc6-dev                \
      libgdbm-dev              \
      libgles2-mesa-dev        \
      libglib2.0-dev           \
      libncursesw5-dev         \
      libreadline-gplv2-dev    \
      libsdl-dev               \
      libsdl2-dev              \
      libsqlite3-dev           \
      libssl-dev               \
      libtool                  \
      locales                  \
      man                      \
      ninja-build              \
      python-pip               \
      python2.7                \
      python2.7-dev            \
      ssh                      \
      texinfo                  \
      tk-dev                   \
      unzip                    \
      wget                     \
      valgrind


# Fix locale.
RUN rm -rf /var/lib/apt/lists/*
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Fetch and configure gclient.
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git ${HOME}/depot_tools
RUN echo export PATH="\${PATH}:\${HOME}/depot_tools" >> ${HOME}/.bashrc
