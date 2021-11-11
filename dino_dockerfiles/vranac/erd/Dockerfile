# NB OSX users: You may encounter docker "memory error" like
#
# ```
# The build process was killed (i.e. SIGKILL). The typical reason for this is
# that there is not enough memory available (e.g. the OS killed a process using
# lots of memory).
# ```
#
# In this case you'll want to give docker more memory than the default (2Gb) in
# order to build `erd`.
#
# To give docker more memory you can:
#  - Find docker in your Menu Bar
#  - Go to Preferences > Resources > Memory
#  - and give docker more memory (eg: 4gb)

FROM haskell:8

LABEL maintainer Srdjan Vranac <vranac@gmail.com>

RUN apt-get update \
    && apt-get install -y graphviz \
    && rm -f /var/cache/apt/archives/*.deb \
    && rm -f /var/cache/apt/archives/partial/*.deb \
    && rm -f /var/cache/apt/*.bin \
    && cabal v2-update \
    && cabal v2-install erd

WORKDIR /erd

ENTRYPOINT ["erd"]