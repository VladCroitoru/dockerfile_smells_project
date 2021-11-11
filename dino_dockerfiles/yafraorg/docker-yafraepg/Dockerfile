#
#  Copyright 2015 yafra.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

#
# yafra.org XMLTV EGP grabber docker
#

# docker build -t yafraepg:latest .
# docker run -d --rm --name yafraepg yafraepg
# docker run -t -i --rm --name yafraepg yafraepg /bin/sh
# docker exec -t -i yafraepg /bin/sh
# docker logs yafraepg
# docker stop yafraepg

# WebGrabPlus version history
# 2017-03-04 Version 2.0
# 2016-07-30 Beta 56.28
# 2016-08-03 Patch 56 - Beta 56.29

# source is yafra os
FROM yafraorg/docker-yafrabase

MAINTAINER Martin Weber <info@yafra.org>

# Install mono packages
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
  apk update && \
  apk upgrade && \
  apk add --update git mono@testing unrar unzip wget curl && \
  apk add --update php7 php7-phar php7-curl && \
  rm -rf /var/cache/apk/*

WORKDIR /work

# setup start script and create directory to store the egpdata file
COPY run-docker.sh /work/run-docker.sh
COPY epgconfig /work/epgconfig
COPY phpserver /work/phpserver

RUN chmod 755 /work/run-docker.sh
RUN mkdir -p /opt/epg

#  wget -q http://www.webgrabplus.com/sites/default/files/download/sw/V1.1.1/upgrade/patchexe_55.zip && \
#   wget -q http://www.webgrabplus.com/sites/default/files/patchexe_prebuild.zip && \
#  git clone https://github.com/yafraorg/docker-yafraepg.git && \

# install web grabber
RUN cd /work && \
  wget -q http://webgrabplus.com/sites/default/files/download/SW/V2.0.0/WebGrabPlus_V2.0_install.tar.gz && \
  tar -zxvf WebGrabPlus_V2.0_install.tar.gz && \
  mv .wg++ wg && \
  cd wg && \
  ./install.sh && \
  cd .. && \
  cp epgconfig/WebGrab++.config.xml wg/ && \
  cp phpserver/horizon.tv.ini wg/siteini.pack/International/ && \
#  cp WebGrab+Plus.exe ../wg && \
#  cd ../docker-yafraepg/epgconfig && \
#  cp -r * /work/wg/. && \
#  cd /work && \
#  rm -rf wgplus/ && \
#  rm -rf repos/ && \
  rm WebGrabPlus_V2.0_install.tar.gz

# expose files via http server
#EXPOSE 8085

#CMD ["/work/run-docker.sh"]
ENTRYPOINT ["/work/run-docker.sh"]