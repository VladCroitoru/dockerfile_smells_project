FROM ocaml/opam:debian

MAINTAINER Yunxing Dai "nov503@gmail.com"

# Install Deps
RUN sudo sh -c 'apt-get update && apt-get install -y --force-yes unzip expect git wget curl && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*'

# Install Android SDK

RUN sudo sh -c 'cd /opt && wget --output-document=android-ndk.zip --quiet https://dl.google.com/android/repository/android-ndk-r12b-linux-x86_64.zip && unzip android-ndk.zip && rm android-ndk.zip'

ENV ANDROID_NDK /opt/android-ndk-r12b

RUN sudo sh -c 'apt-get update && apt-get install -y --force-yes gcc-multilib g++-multilib'

# RUN add-apt-repository ppa:avsm/ppa && apt-get update && apt-get install -y --force-yes opam gcc-multilib g++-multilib
# RUN opam init
RUN sudo -u opam sh -c 'opam repository add android git://github.com/yunxing/opam-cross-android'
RUN sudo -u opam sh -c 'opam switch 4.02.3+32bit'

RUN eval `opam config env`

RUN ARCH=i386 SUBARCH=default SYSTEM=linux_elf \
CCARCH=x86 TOOLCHAIN=x86-4.9 \
TRIPLE=i686-linux-android LEVEL=23 \
STLVER=4.9 STLARCH=x86 \
  opam install conf-android

RUN opam install ocaml-android

RUN opam pin add -y reason 'https://github.com/facebook/reason.git'

# RUN mkdir -p /opt/workspace

# COPY . /opt/workspace

# RUN ls /opt/workspace

RUN echo 'let () = print_endline "Hello, world!"' >helloworld.ml
RUN eval `opam config env` && ocamlfind -toolchain android ocamlopt helloworld.ml -o helloworld.native
RUN file helloworld.o

# Setup environment
# ENV ANDROID_HOME /opt/android-sdk-linux
# ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

# RUN which adb
# RUN which android

# Cleaning
# RUN apt-get clean

# GO to workspace
# RUN mkdir -p /opt/workspace
WORKDIR /workspace
