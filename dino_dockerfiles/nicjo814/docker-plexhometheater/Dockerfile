FROM linuxserver/baseimage

# set env variables
ENV DISPLAY=":0"
ENV XAUTHORITY="/tmp/.docker.xauth"

# specify apt packages to install
ENV BUILD_APTLIST=""
ENV APTLIST="lshw \
plexhometheater"

# add repositories
RUN \
# plex home theater
add-apt-repository ppa:plexapp/plexht

# install packages
RUN apt-get update -q && \
apt-get install \
$APTLIST $BUILD_APTLIST -qy && \

# cleanup 
cd / && \
apt-get purge --remove $BUILD_APTLIST -y && \
apt-get autoremove -y && \
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add some files 
#ADD services/ /etc/service/
#ADD defaults/ /defaults/
ADD init/ /etc/my_init.d/
RUN chmod -v +x /etc/my_init.d/*.sh

# expose ports
#EXPOSE 443

# set volumes
# VOLUME /opt/plexhometheater/share
