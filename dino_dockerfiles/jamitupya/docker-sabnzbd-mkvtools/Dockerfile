FROM linuxserver/sabnzbd
MAINTAINER Speedyyellow


ENV APTLIST="ffmpeg \
mkvtoolnix \
git \
rsync"


# install main packages
RUN add-apt-repository ppa:mc3man/trusty-media && \
apt-get update -q && \
apt-get install \
$APTLIST -qy && \
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# get the mkvdts2ac3 script
RUN git clone https://github.com/JakeWharton/mkvdts2ac3.git /mkvdts2ac3 && chown -R abc:users /mkvdts2ac3
