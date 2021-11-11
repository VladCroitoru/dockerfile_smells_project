FROM debian:latest
MAINTAINER Evan McGee <evan@ringplus.net>

# Install FreeSWITCH
RUN apt-get update && apt-get install -y wget
RUN echo "deb http://files.freeswitch.org/repo/deb/debian/ jessie main" > /etc/apt/sources.list.d/freeswitch.list
RUN wget -O - http://files.freeswitch.org/repo/deb/debian/key.gpg | apt-key add -
RUN apt-get update && \
  apt-get -y upgrade && \
  DEBIAN_FRONTEND=none APT_LISTCHANGES_FRONTEND=none apt-get install -y --force-yes freeswitch-video-deps-most locales debconf
RUN locale-gen en_US en_US.UTF-8
RUN cd /usr/src && git clone https://freeswitch.org/stash/scm/fs/freeswitch.git
RUN cd /usr/src/freeswitch && ./bootstrap.sh -j && ./configure -C 
RUN cd /usr/src/freeswitch && perl -i -pe 's/#applications\/mod_av/applications\/mod_av/g' modules.conf && make && make install
COPY certs /usr/local/freeswitch/certs
RUN rm -rf /usr/src/freeswitch
COPY conf /usr/local/freeswitch
CMD ["/usr/local/freeswitch/bin/freeswitch", "-c", "-nonat"]
