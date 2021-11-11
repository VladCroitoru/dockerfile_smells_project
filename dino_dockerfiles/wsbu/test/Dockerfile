FROM ubuntu

RUN apt-get update && apt-get install --yes --no-install-recommends \
  build-essential \
  ca-certificates \
  cmake \
  git \
  lua5.3 \
  && rm --recursive --force /var/lib/apt/lists/*

# Scripts expect to run via "lua" command
RUN ln -sf /usr/bin/lua5.3 /usr/bin/lua

RUN git clone https://github.com/google/googletest.git /googletest && \
  mkdir /googletest/bin && \
  cd /googletest/bin && \
  cmake .. && \
  make install && \
  cd - && \
  rm --recursive --force /googletest

RUN apt-get purge --yes \
  ca-certificates \
  git \
  && apt-get autoremove --yes
