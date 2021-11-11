FROM ubuntu:16.04
MAINTAINER ZeroC0D3 Team <zeroc0d3.team@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV WINE_MONO_VERSION 4.5.6
ENV WINE_GECKO_VERSION 2.40

#-----------------------------------------------------------------------------
# Install Dependencies
#-----------------------------------------------------------------------------
USER root
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main restricted universe multiverse > /etc/apt/sources.list" \
    && echo "deb-src http://archive.ubuntu.com/ubuntu xenial main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb-src http://archive.ubuntu.com/ubuntu xenial-updates main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb http://archive.ubuntu.com/ubuntu xenial-backports main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb-src http://archive.ubuntu.com/ubuntu xenial-backports main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb http://archive.ubuntu.com/ubuntu xenial-security main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb-src http://archive.ubuntu.com/ubuntu xenial-security main restricted universe multiverse >> /etc/apt/sources.list" \
    && echo "deb http://archive.canonical.com/ubuntu xenial partner >> /etc/apt/sources.list" \
    && echo "deb-src http://archive.canonical.com/ubuntu xenial partner >> /etc/apt/sources.list"

RUN apt-get -y update \
    && DEBIAN_FRONTEND=${DEBIAN_FRONTEND} \
    && apt-get -y install wget \
    && mkdir -p /usr/share/wine/gecko \
    && wget "http://dl.winehq.org/wine/wine-gecko/${WINE_GECKO_VERSION}/wine_gecko-${WINE_GECKO_VERSION}-x86.msi" -O /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86.msi \
    && chmod +x /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86.msi \
    && wget "http://dl.winehq.org/wine/wine-gecko/${WINE_GECKO_VERSION}/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi" -O /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi \
    && chmod +x /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi \
    && mkdir -p /usr/share/wine/mono \
    && wget "http://dl.winehq.org/wine/wine-mono/${WINE_MONO_VERSION}/wine-mono-${WINE_MONO_VERSION}.msi" -O /usr/share/wine/mono/wine-mono-${WINE_MONO_VERSION}.msi \
    && chmod +x /usr/share/wine/mono/wine-mono-${WINE_MONO_VERSION}.msi \
    && apt-get -y remove --purge wget \
    && apt-get -y autoremove --purge \
    && apt-get -y clean  \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

RUN dpkg --add-architecture i386 \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends \
         software-properties-common \
         ca-certificates \
    && add-apt-repository ppa:ubuntu-wine/ppa \
    && apt-get -y update

RUN apt-get -y install --no-install-recommends \
      curl \
      dosbox \
      p7zip \
      p7zip-full \
      x11vnc \
      xvfb \
      wget

RUN apt-get -y install --no-install-recommends \
      wine1.8 \
      winetricks \
      winbind

#-----------------------------------------------------------------------------
# Cleanup Installation
#-----------------------------------------------------------------------------
RUN apt-get -y remove --purge software-properties-common \
    && apt-get -y autoremove --purge \
    && apt-get -y clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

#-----------------------------------------------------------------------------
# Create User
#-----------------------------------------------------------------------------
ENV USERNAME wine
RUN useradd -u 1001 -d /home/${USERNAME} -m -s /bin/bash wine \
    && mkdir /tmp/.X11-unix \
    && chmod 1777 /tmp/.X11-unix

USER ${USERNAME}
ENV HOME /home/${USERNAME} \
    WINEPREFIX /home/${USERNAME}/.wine \
    WINEARCH win32 \
    WINEDEBUG -all

WORKDIR ${HOME}
# RUN echo "alias winegui='wine explorer /desktop=DockerDesktop,1024x768'" > ~/.bash_aliases

#-----------------------------------------------------------------------------
# Run Docker Container
#-----------------------------------------------------------------------------
CMD []