# set base os
FROM phusion/baseimage:0.9.15
ENV DEBIAN_FRONTEND noninteractive
# Set correct environment variables
ENV HOME /root

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Configure user nobody to match unRAID's settings
RUN \
usermod -u 99 nobody && \
usermod -g 100 nobody && \
usermod -d /home nobody && \
chown -R nobody:users /home && \

# Install Dependencies ,add startup files and patchfile
mkdir -p /root/advancestore && \
mkdir /etc/service/xbmc
ADD src/kodi.sh /etc/service/xbmc/run
ADD src/advancedsettings.xml /advancestore/
ADD src/firstrun.sh /etc/my_init.d/firstrun.sh
RUN chmod +x /etc/service/xbmc/run && \
chmod +x /etc/my_init.d/firstrun.sh && \
apt-get update && \
apt-get install -y git openjdk-7-jre-headless build-essential gawk pmount libtool nasm yasm automake cmake gperf zip unzip bison libsdl-dev libsdl-image1.2-dev libsdl-gfx1.2-dev libsdl-mixer1.2-dev libfribidi-dev liblzo2-dev libfreetype6-dev libsqlite3-dev libogg-dev libasound2-dev python-sqlite libglew-dev libcurl3 libcurl4-gnutls-dev libxrandr-dev libxrender-dev libmad0-dev libogg-dev libvorbisenc2 libsmbclient-dev libmysqlclient-dev libpcre3-dev libdbus-1-dev libjasper-dev libfontconfig-dev libbz2-dev libboost-dev libenca-dev libxt-dev libxmu-dev libpng-dev libjpeg-dev libpulse-dev mesa-utils libcdio-dev libsamplerate-dev libmpeg3-dev libflac-dev libiso9660-dev libass-dev libssl-dev fp-compiler gdc libmpeg2-4-dev libmicrohttpd-dev libmodplug-dev libssh-dev gettext cvs python-dev libyajl-dev libboost-thread-dev libplist-dev libusb-dev libudev-dev libtinyxml-dev libcap-dev autopoint libltdl-dev swig libgtk2.0-bin libtag1-dev libtiff-dev libnfs1 libnfs-dev libxslt-dev libbluray-dev software-properties-common python-software-properties && \
add-apt-repository ppa:team-xbmc/ppa && \
apt-get update && \
apt-get install -y kodi-eventclients-xbmc-send && \
add-apt-repository --remove ppa:team-xbmc/ppa && \

# Download XBMC, pick version from github
git clone https://github.com/topfs2/xbmc.git && \
cd xbmc && \
git checkout helix_headless && \
# Configure, make, clean.
 ./bootstrap && \
./configure \
--enable-nfs \
--enable-upnp \
--enable-ssh \
--enable-libbluray \
--disable-debug \
--disable-vdpau \
--disable-vaapi \
--disable-crystalhd \
--disable-vdadecoder \
--disable-vtbdecoder \
--disable-openmax \
--disable-joystick \
--disable-rsxs \
--disable-projectm \
--disable-rtmp \
--disable-airplay \
--disable-airtunes \
--disable-dvdcss \
--disable-optical-drive \
--disable-libusb \
--disable-libcec \
--disable-libmp3lame \
--disable-libcap \
--disable-udev \
--disable-libvorbisenc \
--disable-asap-codec \
--disable-afpclient \
--disable-goom \
--disable-fishbmc \
--disable-spectrum \
--disable-waveform \
--disable-avahi \
--disable-non-free \
--disable-texturepacker \
--disable-pulse \
--disable-dbus \
--disable-alsa \
--disable-hal \
--prefix=/opt/kodi-server && \
make && \
make install && \
apt-get purge -y --auto-remove git openjdk* build-essential gcc gawk pmount libtool nasm yasm automake cmake gperf zip unzip bison libsdl-dev libsdl-image1.2-dev libsdl-gfx1.2-dev libsdl-mixer1.2-dev libfribidi-dev liblzo2-dev libfreetype6-dev libsqlite3-dev libogg-dev libasound2-dev python-sqlite libglew-dev libcurl3 libcurl4-gnutls-dev libxrandr-dev libxrender-dev libmad0-dev libogg-dev libvorbisenc2 libsmbclient-dev libmysqlclient-dev libpcre3-dev libdbus-1-dev libjasper-dev libfontconfig-dev libbz2-dev libboost-dev libenca-dev libxt-dev libxmu-dev libpng-dev libjpeg-dev libpulse-dev mesa-utils libcdio-dev libsamplerate-dev libmpeg3-dev libflac-dev libiso9660-dev libass-dev libssl-dev fp-compiler gdc libmpeg2-4-dev libmicrohttpd-dev libmodplug-dev libssh-dev gettext cvs python-dev libyajl-dev libboost-thread-dev libplist-dev libusb-dev libudev-dev libtinyxml-dev libcap-dev autopoint libltdl-dev swig libgtk2.0-bin libtag1-dev libtiff-dev libnfs-dev libbluray-dev software-properties-common python-software-properties && \
apt-get -y autoremove && \
apt-get install -y fonts-liberation libaacs0 libbluray1 libasound2 libass4 libasyncns0 libavcodec54 libavfilter3 libavformat54 libavutil52 libcaca0 libcap2 libcdio13 libcec2 libcrystalhd3 libdrm-nouveau2 libenca0 libflac8 libfontenc1 libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libglew1.10 libglu1-mesa libgsm1 libice6 libjson0 liblcms1 libllvm3.5 liblzo2-2 libmad0 libmicrohttpd10 libmikmod2 libmodplug1 libmp3lame0 libmpeg2-4 libmysqlclient18 liborc-0.4-0 libpcrecpp0 libplist1 libpostproc52 libpulse0 libpython2.7 libschroedinger-1.0-0 libsdl-mixer1.2 libsdl1.2debian libshairport1 libsm6 libsmbclient libsndfile1 libspeex1 libswscale2 libtalloc2 libtdb1 libtheora0 libtinyxml2.6.2 libtxc-dxtn-s2tc0 libva-glx1 libva-x11-1 libva1 libvdpau1 libvorbisfile3 libvpx1 libwbclient0 libwrap0 libx11-xcb1 libxaw7 libxcb-glx0 libxcb-shape0 libxmu6 libxpm4 libxt6 libxtst6 libxv1 libxxf86dga1 libxxf86vm1 libyajl2 mesa-utils mysql-common python-cairo python-gobject-2 python-gtk2 python-imaging python-support tcpd ttf-liberation libssh-4 libtag1c2a libcurl3-gnutls libnfs1 && \
apt-get -y autoremove && \
apt-get clean && \
cd / && \
rm -rf  xbmc && \
chown -R nobody:users /opt/kodi-server && \
chown -R nobody:users /advancestore && \
rm -rf /var/lib/apt/lists /usr/share/man /usr/share/doc
# set ports
EXPOSE 9777/udp 8080/tcp
