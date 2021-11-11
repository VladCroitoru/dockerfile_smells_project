FROM turchinc/xenial-libreoffice 

LABEL tag="turchinc/xenial-imagemagick" vendor="Bertsch Innovation GmbH"
MAINTAINER Chris Turchin <chris.turchin@bertschinnovation.com>
ENV DEBIAN_FRONTEND noninteractive

# gs && ffmpeg && dcraw seem to all be available from common repositories
# grab im dev packages, then build from source...
# ref: https://www.imagemagick.org/discourse-server/viewtopic.php?t=29006
RUN 	apt-get update && \
	apt-get install -y wget dcraw ffmpeg ghostscript libmagick++-dev 
RUN cd /tmp && wget http://www.imagemagick.org/download/ImageMagick.tar.gz 
RUN cd /tmp && tar xzf ImageMagick.tar.gz 
RUN cd /tmp/ImageMagick* && ./configure && make &&  make install && ldconfig /usr/local
ADD policy.xml /etc/ImageMagick-6/policy.xml
# Clean the cache created by package installations
RUN 	apt-get autoclean && apt-get --purge -y autoremove && \
		apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

