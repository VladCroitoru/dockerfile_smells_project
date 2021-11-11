FROM ubuntu:15.04
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y xorg nano locate zsh supervisor logrotate git curl wget tightvncserver openssh-server \
    lxde-core lxappearance lxterminal firefox lubuntu-icon-theme lubuntu-artwork-15-04 lubuntu-lxpanel-icons lubuntu-artwork \
    xfonts-100dpi xfonts-100dpi-transcoded xfonts-75dpi xfonts-75dpi-transcoded xfonts-base \
 && rm -rf /var/lib/apt/lists/*

COPY assets/install /opt/install
RUN chmod 755 /opt/install
RUN /opt/install

COPY assets/init /opt/init
RUN chmod 755 /opt/init

VOLUME ["/home/vnc/share"]
WORKDIR /home/vnc

ENTRYPOINT ["/opt/init"]
CMD ["start"]

EXPOSE 22 5901-5999
