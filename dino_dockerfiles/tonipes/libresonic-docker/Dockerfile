#
# Dockerfile for libresonic
#
# https://github.com/tonipes/libresonic-docker
#
# https://github.com/Libresonic/libresonic
#

FROM tomcat:8

MAINTAINER Toni Pesola

# Install libs for transcoding
RUN apt-get update && \
	  apt-get install --yes --force-yes --no-install-recommends --no-install-suggests flac && \
	  apt-get install --yes --force-yes --no-install-recommends --no-install-suggests lame && \
	  apt-get install --yes --force-yes --no-install-recommends --no-install-suggests libav-tools

# Download and setup libresonic
RUN rm -rf /usr/local/tomcat/webapps && mkdir /usr/local/tomcat/webapps

RUN wget https://libresonic.org/release/libresonic-v6.2.war -O /usr/local/tomcat/webapps/ROOT.war

# Setup transcoding libs so that libresonic can use them
RUN mkdir -p /var/libresonic/transcode

RUN cd /var/libresonic/transcode && ln -s "$(which flac)"

RUN cd /var/libresonic/transcode && ln -s "$(which lame)"

RUN cd /var/libresonic/transcode && ln -s "$(which avconv)" ffmpeg
