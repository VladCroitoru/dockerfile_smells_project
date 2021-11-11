FROM ubuntu:trusty

MAINTAINER Jon Borgonia "jon@gomagames.com"

ENV DEBIAN_FRONTEND noninteractive

ENV HAXE_DOWNLOAD_URL https://github.com/HaxeFoundation/haxe/releases/download/3.4.2/haxe-3.4.2-linux64.tar.gz
ENV NEKO_DOWNLOAD_URL http://nekovm.org/media/neko-2.1.0-linux64.tar.gz

# Haxe environment variables
ENV HAXE_STD_PATH /usr/lib/haxe/std/
ENV PATH /usr/lib/haxe/:$PATH
# Neko environment variables
ENV NEKOPATH /usr/lib/neko/
ENV LD_LIBRARY_PATH /usr/lib/neko/
ENV PATH /usr/lib/neko/:$PATH

RUN apt-get update && \
    apt-get install -y curl build-essential libgc-dev

# Download and install haxe
RUN curl -L $HAXE_DOWNLOAD_URL | tar xz -C /root/ && \
  mv /root/haxe* /usr/lib/haxe && \
  curl -L $NEKO_DOWNLOAD_URL | tar xz -C /root && \
  mv /root/neko* /usr/lib/neko && \
  ln -sf /usr/lib/haxe/haxe /usr/bin/haxe && \
  ln -sf /usr/lib/haxe/haxelib /usr/bin/haxelib && \
  ln -sf /usr/lib/neko/neko /usr/bin/neko && \
  ln -sf /usr/lib/neko/nekoc /usr/bin/nekoc && \
  ln -sf /usr/lib/neko/nekotools /usr/bin/nekotools && \
  ln -sf /usr/lib/neko/nekoml /usr/bin/nekoml

RUN mkdir /usr/lib/haxelib && \
  haxelib setup /usr/lib/haxelib && \
  rm -rf /var/lib/apt/lists/*

RUN haxelib install hxcpp
