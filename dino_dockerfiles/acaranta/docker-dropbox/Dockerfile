FROM ubuntu:14.04
MAINTAINER arthur@caranta.com
RUN apt-get update && apt-get install -y psmisc curl libatomic1 libglib2.0-0
RUN apt-get install -y libglapi-mesa  libxdamage1 libxfixes3 libxcb-glx0 libxcb-dri2-0 libxcb-dri3-0 libxcb-present0 libxcb-sync1 libxshmfence1 libxxf86vm1
RUN mkdir /root/.dropbox-dist && touch /root/.dropbox-dist/VERSION

# Add Tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

ADD getdropbox.sh /
RUN /getdropbox.sh

WORKDIR /root

CMD while true ; do /getdropbox.sh ; echo "Cleaning Dropbox Processes" ;killall -9 $(ls /root/.dropbox-dist/dropbox-lnx*/dropbox) ; killall -9 /root/.dropbox-dist/dropboxd; echo "Restarting Dropbox" ; /root/.dropbox-dist/dropboxd ; sleep 5 ; done
