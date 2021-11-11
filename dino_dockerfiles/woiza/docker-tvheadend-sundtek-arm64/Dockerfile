FROM lsiobase/xenial.arm64

LABEL maintainer="woiza"

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"

# adding qemu for crossbuilding on DockerHub
#COPY --from=resin/aarch64-alpine:latest /usr/bin/qemu* /usr/bin/
#COPY --from=resin/aarch64-alpine:latest /usr/bin/resin-xbuild* /usr/bin/
#COPY --from=resin/aarch64-alpine:latest /usr/bin/cross-build* /usr/bin/

COPY --from=resin/aarch64-alpine:latest ["/usr/bin/qemu*", "/usr/bin/resin-xbuild*", "/usr/bin/cross-build*",  "/usr/bin/"]

RUN [ "cross-build-start" ]
# Install dependencies


RUN apt-get update -y &&\ 
  apt-get install -y \
  apt-transport-https \
  software-properties-common \
  bzip2 \
  libavahi-client3 \
  libav-tools \
  xmltv \
  wget \
  gnupg2 \
  udev \
  debconf-utils &&\ 

# Add key and tvheadend repository
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 379CE192D401AB61
#RUN apt-add-repository "https://dl.bintray.com/tvheadend/deb ${tvh_release}"


# Install tvheadend

apt-add-repository ppa:mamarley/tvheadend-git-stable &&\ 

echo "tvheadend tvheadend/admin_password password admin" | debconf-set-selections && \
	echo "tvheadend tvheadend/admin_username string admin" | debconf-set-selections &&\ 

apt-get update -y &&  \ 
apt-get install -y tvheadend &&\ 

# Install Sundtek DVB Driver
wget http://www.sundtek.de/media/sundtek_netinst.sh && \
  chmod 777 sundtek_netinst.sh && \
 ./sundtek_netinst.sh -easyvdr && \

# Create Locales
#ENV LANG="de_DE.UTF-8"
#RUN apt-get update -y && apt-get install -y locales && $_apt_clean \
# && grep "$LANG" /usr/share/i18n/SUPPORTED >> /etc/locale.gen && locale-gen \
# && update-locale LANG=$LANG

echo "**** cleanup ****" && \
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*


RUN [ "cross-build-end" ]

COPY root/ /

# Default container settings
VOLUME /config /recordings /picons
EXPOSE 9981 9982
