FROM codafog/kodi-compiler-rpi:base

RUN [ "cross-build-start" ]

# CPU argument for Raspberry Pi 2 or 3
ARG CPU=cortex-a7
# CPU argument for Raspberry Pi 0
#ARG CPU=arm1176jzf-s

# test kodi 17 piplware branch krypton_new
ARG GITURL="git://github.com/PIPplware/xbmc"
ARG GITBRANCH="krypton_new"

# test kodi 18 piplware branch newclock5
#ARG GITURL="git://github.com/PIPplware/xbmc"
#ARG GITBRANCH="newclock5"

# get sources with git
RUN mkdir -p /src/kodi/
WORKDIR /src/kodi/

RUN git clone --depth 1 "$GITURL" --branch "$GITBRANCH" /src/kodi

# Download the script that compile and build the kodi package
#RUN wget -q https://raw.githubusercontent.com/nsenica/xbmc/krypton_new/tools/Linux/packaging/build_rpi_debian_packages.sh \
RUN wget -q https://raw.githubusercontent.com/PIPplware/xbmc/krypton_new/tools/Linux/packaging/build_rpi_debian_packages.sh \
  && chmod +x build_rpi_debian_packages.sh && sed -i 's/EXTRA_FLAGS="/EXTRA_FLAGS="-DRPI=1 /g' build_rpi_debian_packages.sh

# uncomment to remove some options for Kodi
#RUN sed -i 's/DENABLE_MMAL=ON/DENABLE_MMAL=AUTO/g' build_rpi_debian_packages.sh 
#RUN sed -i 's/DENABLE_DVDCSS=ON/DENABLE_DVDCSS=AUTO/g' build_rpi_debian_packages.sh 
#RUN sed -i 's/DENABLE_MYSQLCLIENT=ON/DENABLE_MYSQLCLIENT=AUTO/g' build_rpi_debian_packages.sh 
#RUN sed -i 's/DENABLE_LIRC=ON/DENABLE_LIRC=AUTO/g' build_rpi_debian_packages.sh 
#RUN sed -i 's/DENABLE_BLURAY=ON/DENABLE_BLURAY=AUTO/g' build_rpi_debian_packages.sh 
#RUN sed -i 's/DENABLE_AIRTUNES=ON/DENABLE_AIRTUNES=OFF/g' build_rpi_debian_packages.sh 

# compile tools
RUN cd tools/depends && ./bootstrap &&  \
   ./configure --with-platform=raspberry-pi2 --host=arm-linux-gnueabihf --prefix=/opt/xbmc-deps --with-tarballs=/opt/xbmc-tarballs \
   && make

# compile Kodi
RUN ./build_rpi_debian_packages.sh

RUN [ "cross-build-end" ]
#RUN mkdir build && cd build && CXXFLAGS="-DRPI=1" CFLAGS="-DRPI=1" cmake \
#-DVERBOSE=1 \
#-DCORE_SYSTEM_NAME=rbpi \
#-DENABLE_MMAL=ON \
#-DENABLE_OPENGL=OFF \
#-DWITH_CPU=${CPU} \
#-DCMAKE_PREFIX_PATH=/opt/vc \
#-DENABLE_OPENGLES=ON \
#-DCMAKE_BUILD_TYPE=Release \
#-DCMAKE_INSTALL_PREFIX=/usr \
#-DENABLE_AIRTUNES=ON \
#-DENABLE_ALSA=ON \
#-DENABLE_AVAHI=ON \
#-DENABLE_BLURAY=ON \
#-DENABLE_CEC=ON \
#-DENABLE_DBUS=ON \
#-DENABLE_DVDCSS=ON \
#-DENABLE_EGL=ON \
#-DENABLE_EVENTCLIENTS=ON \
#-DENABLE_INTERNAL_FFMPEG=ON \
#-DENABLE_INTERNAL_CROSSGUID=ON \
#-DENABLE_MICROHTTPD=ON \
#-DENABLE_MYSQLCLIENT=ON \
#-DENABLE_NFS=ON \
#-DENABLE_NONFREE=ON \
#-DENABLE_OPENSSL=ON \
#-DENABLE_OPTICAL=ON \
#-DENABLE_PULSEAUDIO=ON \
#-DENABLE_SMBCLIENT=ON \
#-DENABLE_SSH=ON \
#-DENABLE_UDEV=ON \
#-DENABLE_UPNP=ON \
#-DENABLE_VAAPI=OFF \
#-DENABLE_VDPAU=OFF \
#-DENABLE_X11=OFF \
#-DENABLE_XSLT=ON \
#-DENABLE_LIRC=ON \
#-DCPACK_GENERATOR=DEB \
#-DDEBIAN_PACKAGE_VERSION=1~ \
#-DDEB_PACKAGE_ARCHITECTURE=armhf \
#../project/cmake/
#
#RUN cd build && cmake --build . -- VERBOSE=1 -j`nproc` #KO
#RUN cd build && cpack

#RUN cd build && dpkg -i packages/*.deb

# install debian packages
#RUN dpkg -i packages/*.deb

# uncomment if you want to enable webserver and remote control settings
#COPY "./files-to-copy-to-image/settings.xml" "/usr/share/kodi/system/settings"

# ports and volumes
#VOLUME /config/kodi
#VOLUME /data
#EXPOSE 8080 9777/udp

#CMD ["bash", "/usr/bin/kodi-standalone"]

#RUN [ "cross-build-end" ]
