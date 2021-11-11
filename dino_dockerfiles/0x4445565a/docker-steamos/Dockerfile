FROM ubuntu:16.04

ENV TERM $TERM

RUN apt-get update && \
  apt-get install -y zenity \
  alsa-utils \
  python \
  curl \
  python-apt \
  pulseaudio \
  pciutils \
  xterm \
  xz-utils \
  sudo

RUN apt-get install -y alsa-base

RUN dpkg --add-architecture i386 && apt-get update && \
    apt-get install -yq \
      wget \
      libgl1-mesa-dri:i386 \
      libgl1-mesa-glx:i386 \
      libc6:i386 \
      libstdc++6:i386 \
      libtxc-dxtn-s2tc0:i386

RUN rm -rf /var/lib/apt/lists/*

RUN echo options snd_hda_intel index=1 >> /etc/modprobe.d/default.conf

RUN wget http://media.steampowered.com/client/installer/steam.deb
RUN dpkg -i --force-all steam.deb && rm -f steam.deb

RUN echo 'steam ALL = NOPASSWD: ALL' > /etc/sudoers.d/steam && chmod 0440 /etc/sudoers.d/steam

RUN adduser --disabled-password --gecos 'Steam' steam && \
  adduser steam video

USER steam

ENV DISPLAY $DISPLAY
ENV HOME /home/steam
VOLUME /home/steam

# Commented out for ease of development
#CMD ["steam"]
