FROM fedora:23

#####
# TODO
#
# 1) Is there a way to hardcode the subsonic premium license key?
# 2) Add personal user account
# 3) Make passwords dynamic
# 4) Pass volumes in dynamically
#
#####

#####
# Install Packages
#####

RUN dnf -y install \
java-1.8.0-openjdk \
wget

#####
# Install and Configure Subsonic service
#####

RUN wget http://www.subsonic.org/pages/download2.jsp?target=subsonic-6.0.beta1.rpm
RUN groupadd -g 1001 media

RUN groupadd -g 1002 subsonic && \
useradd subsonic -g subsonic && \
usermod -a -G media subsonic && \
echo "subsonic:subsonic" | chpasswd


EXPOSE 4040

#####
# Configure Storage
#####
VOLUME [ "/sys/fs/cgroup" ]

VOLUME /config
VOLUME /data

#####
# Configure application executable
#####

CMD ["/usr/bin/subsonic --context-path=/subsonic --max-memory=200 --port=0 --https-port=4040 --home=/data --default-podcast-folder=/data/podcasts --default-playlist-folder=/data/playlists --default-music-folder=/data/music"]

#####
# Clean up
#####

RUN dnf clean all