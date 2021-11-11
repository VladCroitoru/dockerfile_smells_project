FROM ubuntu:16.04

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install --no-install-recommends -y software-properties-common python-software-properties && \
    add-apt-repository ppa:ubuntu-wine/ppa -y && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \
    apt-get update && \
    apt-get install --no-install-recommends -y git nodejs npm wine1.8 osslsigncode mono-devel ca-certificates-mono && \
    ln -s /usr/bin/nodejs /usr/bin/node
