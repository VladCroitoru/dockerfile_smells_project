# https://freeswitch.org/confluence/display/FREESWITCH/FreeSWITCH+1.6+Video
FROM debian:jessie
MAINTAINER Ian Blenke <ian@blenke.com>

RUN perl -pi -e 's/httpredir.debian.org/cloudfront.debian.net/g' /etc/apt/sources.list
RUN apt-get update -y
RUN DEBIAN_FRONTEND=none APT_LISTCHANGES_FRONTEND=none apt-get install -y wget

RUN echo "deb http://files.freeswitch.org/repo/deb/debian/ jessie main" > /etc/apt/sources.list.d/99FreeSWITCH.test.list
RUN wget -O - http://files.freeswitch.org/repo/deb/debian/key.gpg |apt-key add -
RUN apt-get update -y

RUN DEBIAN_FRONTEND=none APT_LISTCHANGES_FRONTEND=none apt-get install -y --force-yes freeswitch-video-deps-most

# because we're in a branch that will go through many rebases it's
# better to set this one, or you'll get CONFLICTS when pulling (update)
RUN git config --global pull.rebase true
 
RUN git clone https://freeswitch.org/stash/scm/fs/freeswitch.git freeswitch.git

WORKDIR freeswitch.git

RUN ./bootstrap.sh -j
RUN ./configure -C

RUN perl -i -pe 's/#formats\/mod_vlc/formats\/mod_vlc/g' modules.conf
RUN perl -i -pe 's/#applications\/mod_av/applications\/mod_av/g' modules.conf

RUN make
RUN make install
RUN make cd-sounds-install cd-moh-install samples

ADD vid.conf /etc/sysctl.d/vid.conf

ENV FREESWITCH_PATH /usr/local/freeswitch

WORKDIR /usr/local/freeswitch

ENV PATH /usr/local/freeswitch/bin:$PATH

RUN useradd --system --home-dir ${FREESWITCH_PATH} --comment "FreeSWITCH Voice Platform" --groups daemon freeswitch && \
    chown -R freeswitch:daemon ${FREESWITCH_PATH} && \
    chmod -R ug=rwX,o= ${FREESWITCH_PATH} && \
    chmod -R u=rwx,g=rx ${FREESWITCH_PATH}/bin/*

# Force any derived images to use the freeswitch user.. on second thought, let's not impose that on this base image
#ONBUILD USER freeswitch

CMD /usr/local/freeswitch/bin/freeswitch -c

