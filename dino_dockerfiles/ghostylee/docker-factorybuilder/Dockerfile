FROM ubuntu:12.04
MAINTAINER Li Song "ghosty.lee.1984@gmail.com"

# timesys host requirements
ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-reconfigure -p critical dash

COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y --force-yes \
        automake binutils-dev bison build-essential bzip2 ecj fastjar \
        flex gawk gconf2 gettext gperf groff gtk-doc-tools guile-1.8 icon-naming-utils indent \
        libc6-dev libdbus-glib-1-dev libexpat1-dev libglade2-dev libgmp3-dev libgtk2.0-bin \
        libgtk2.0-dev libmpfr-dev libncurses5-dev libperl-dev libsdl1.2-dev libtool libusb-dev \
        libxml-parser-perl lzop python-dev python-libxml2 ruby scons sharutils swig texinfo \
        texlive-extra-utils texlive-latex3 unzip wget x11-xkb-utils zip zlib1g \
        lib32ncurses5 lib32z1 lib32z1-dev libc6-dev-i386 ia32-libs sudo bc \
        cmake libcppunit-dev gcc-4.9 g++-4.9 libprotobuf-dev

RUN ln -sfn /bin/bash /bin/sh

RUN mkdir -p /home/worker && \
    mkdir -p /home/worker/building && \
    echo "worker:x:1000:1000:worker,,,:/home/worker:/bin/bash" >> /etc/passwd && \
    echo "worker:x:1000:" >> /etc/group && \
    echo "worker ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/worker && \
    chmod 0440 /etc/sudoers.d/worker && \
    chown worker:worker -R /home/worker && \
    chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo

USER worker
ENV HOME /home/worker
WORKDIR /home/worker/building
CMD /bin/bash
