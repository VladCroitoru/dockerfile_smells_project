FROM ubuntu:xenial

MAINTAINER Steve Russo <svrusso1@gmail.com>

RUN apt-get update && apt-get install -y aria2

ADD https://raw.githubusercontent.com/ilikenwf/apt-fast/master/apt-fast /usr/bin/apt-fast

ADD https://raw.githubusercontent.com/ilikenwf/apt-fast/master/apt-fast.conf /usr/bin/apt-fast.conf

RUN chmod +x /usr/bin/apt-fast

RUN apt-fast install -y \
  checkinstall build-essential git-core cmake libssl-dev libx11-dev libxext-dev libxinerama-dev \
  libxcursor-dev libxdamage-dev libxv-dev libxkbfile-dev libasound2-dev libcups2-dev libxml2 libxml2-dev \
  libxrandr-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \
  libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libxi-dev libavutil-dev \
  libavcodec-dev libxtst-dev libgtk-3-dev libgcrypt11-dev libssh-dev libpulse-dev \
  libvte-2.91-dev libxkbfile-dev libfreerdp-dev libtelepathy-glib-dev libjpeg-dev \
  libgnutls-dev libgnome-keyring-dev libavahi-ui-gtk3-dev libvncserver-dev \
  libappindicator3-dev intltool libsecret-1-dev libwebkit2gtk-4.0-dev libsystemd-dev
  
RUN apt-get --purge remove -y freerdp-x11 \
 remmina remmina-common remmina-plugin-rdp remmina-plugin-vnc remmina-plugin-gnome \
 remmina-plugin-nx remmina-plugin-telepathy remmina-plugin-xdmcp

RUN apt-get --purge remove -y libfreerdp-dev libfreerdp-plugins-standard libfreerdp1 \
 libfreerdp-utils1.1 libfreerdp-primitives1.1 libfreerdp-locale1.1 \
 libfreerdp-gdi1.1 libfreerdp-crypto1.1 libfreerdp-core1.1 libfreerdp-common1.1.0 \
 libfreerdp-codec1.1 libfreerdp-client1.1 libfreerdp-cache1.1

RUN apt-get --purge remove -y \
  libfreerdp-rail1.1 libwinpr-asn1-0.1 libwinpr-bcrypt0.1 libwinpr-credentials0.1 libwinpr-credui0.1 \
  libwinpr-crt0.1 libwinpr-crypto0.1 libwinpr-dev libwinpr-dsparse0.1 libwinpr-environment0.1 \
  libwinpr-error0.1 libwinpr-file0.1 libwinpr-handle0.1 libwinpr-heap0.1 libwinpr-input0.1 \
  libwinpr-interlocked0.1 libwinpr-io0.1 libwinpr-library0.1 libwinpr-path0.1 libwinpr-pipe0.1 \
  libwinpr-pool0.1 libwinpr-registry0.1 libwinpr-rpc0.1 libwinpr-sspi0.1 libwinpr-sspicli0.1 \
  libwinpr-synch0.1 libwinpr-sysinfo0.1 libwinpr-thread0.1 libwinpr-timezone0.1 libwinpr-utils0.1 \
  libwinpr-winhttp0.1 libwinpr-winsock0.1
  
ADD build.sh /build.sh

CMD [ "/bin/bash" ]
