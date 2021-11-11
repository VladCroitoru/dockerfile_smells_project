FROM debian:stable

MAINTAINER Christian Brauner christianvanbrauner[at]gmail.com

RUN export DEBIAN_FRONTEND=noninteractive \
&& cd /etc/dpkg/dpkg.cfg.d \
&& printf '\npath-exclude=/usr/share/locale/*' >> excludes \
&& printf '\npath-include=/usr/share/locale/en*' >> excludes \
&& printf '\npath-include=/usr/share/locale/locale.alias' >> excludes \
&& printf '\npath-exclude=/usr/share/man/*' >> excludes \
&& printf '\npath-include=/usr/share/man/en*' >> excludes \
&& printf '\npath-include=/usr/share/man/man[1-9]/*' >> excludes \
&& cd /etc/apt/sources.list.d \
&& printf '\ndeb http://neurodebian.g-node.org data main contrib non-free' > neurodebian.sources.list \
&& printf '\ndeb-src http://neurodebian.g-node.org data main contrib non-free' >> neurodebian.sources.list \
&& printf '\ndeb http://neurodebian.g-node.org wheezy main contrib non-free' >> neurodebian.sources.list \
&& printf '\ndeb-src http://neurodebian.g-node.org wheezy main contrib non-free\n' >> neurodebian.sources.list \
&& apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 2649A5A9 \
&& apt-get update -qq -y \
&& apt-get install -y --no-install-recommends \
# Sound
   alsa-base \
   alsa-utils \
   alsa-oss \
   bash-completion \
   ca-certificates \
   git \
   locales \
   less \
   mupdf \
   sudo \
   wget \
   zip \
   unzip \
# 3D
   libegl1-mesa \
   libgl1-mesa-dri \
   libgl1-mesa-glx \
   libopenvg1-mesa \
   libglu1-mesa-dev \
   mesa-utils \
# Sound
   alsa-base \
   alsa-utils \
   alsa-oss \
   flac \
# Psychopy deps
   libavbin-dev \
   libavbin0 \
   python \
   python-setuptools \
   python-numpy \
   python-scipy \
   python-pyglet \
   python-wxgtk2.8 \
   python-wxtools \
   python-wxversion \
   python-imaging \
   python-matplotlib \
   python-lxml \
   python-openpyxl \
   python-pyo \
# Psychopy opt deps
   python-optcomplete \
   python-pypsignifit \
   python-parallel \
   python-pp \
   python-pytest \
   python-serial \
   python-sphinx \
   python-tk \
&& echo 'root:test' | chpasswd \
&& useradd -u 1000 -m docker \
&& echo 'docker:test' | chpasswd \
&& usermod -s /bin/bash docker \
&& usermod -a -G 100 docker \
&& usermod -a -G sudo docker \
# set correct GID should your distro differ
# && groupmod -g 91 video \
&& usermod -a -G video docker \
# set correct GID should your distro differ
# && groupmod -g 92 audio \
&& usermod -a -G audio docker \
&& apt-get clean \
&& cd /var/lib/apt/lists \
&& rm -rf *

ENV HOME /home/docker
ENV PYTHONPATH /home/docker/psychopy
WORKDIR /home/docker
USER docker

RUN cd /home/docker \
&& git clone https://github.com/psychopy/psychopy.git
