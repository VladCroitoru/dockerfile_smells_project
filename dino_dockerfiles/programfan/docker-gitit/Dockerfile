#
# Dockerfile
#

FROM debian:8
LABEL maintainer="Yang Zhang <zyangmath@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive
# The following command installs custom ghc and use cabal to install gitit
# into system path. The building tools and intermediate haskell libraries are
# then removed to keep the image slim. The custom ghc installation is copied
# from library/haskell. We do not inherite from library/haskell because the
# final image would become very large (2.4G).
ENV ORIG_PATH $PATH
ENV PATH /opt/cabal/1.24/bin:/opt/ghc/8.0.2/bin:/opt/happy/1.19.5/bin:/opt/alex/3.1.7/bin:$PATH
ENV LANG C
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    echo 'deb http://ftp.debian.org/debian jessie-backports main' \
        >/etc/apt/sources.list.d/backports.list && \
    echo 'deb http://ppa.launchpad.net/hvr/ghc/ubuntu trusty main' \
        >/etc/apt/sources.list.d/ghc.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F6F88286 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        git locales supervisor gosu  \
        cabal-install-1.24 ghc-8.0.2 happy-1.19.5 alex-3.1.7 \
        zlib1g-dev libtinfo-dev libsqlite3-0 libsqlite3-dev \
        ca-certificates g++ && \
    cabal update && cabal install --prefix=/usr/local gitit && \
    cabal install --reinstall --prefix=/usr/local --ghc-options="-rtsopts" \
        gitit && \
    apt-get purge -y --auto-remove \
        cabal-install-1.24 ghc-8.0.2 happy-1.19.5 alex-3.1.7 \
        zlib1g-dev libtinfo-dev libsqlite3-dev ca-certificates g++ && \
    rm -rf /root/.cabal /root/.stack /root/.ghc && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/local/bin/*.md /usr/local/bin/doc && \
    rm -rf /usr/local/bin/pandoc /usr/local/bin/yaml2json \
        /usr/local/bin/json2yaml && \
    rm -rf /usr/local/lib/x86_64-linux-ghc-8.0.2
ENV PATH /usr/local/bin:$ORIG_PATH

# Use an UTF-8 locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

# Basic system settings
RUN echo "root:123456" | chpasswd
