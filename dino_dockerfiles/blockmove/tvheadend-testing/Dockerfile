# -----------------------------------------------------------------------------
# blockmove/tvheadend
#
# docker build -f Dockerfile -t blockmove/tvheadend-testing .
## 2017-06-11 - Added tzdata to apt-get -y install
## 2016-04-17 : Init Project
# -----------------------------------------------------------------------------


FROM phusion/baseimage

MAINTAINER Dieter Poesl <doc@poesl-online.de>

# Set Enviroment
# Skip install dialogues
# Home-Directory
ENV DEBIAN_FRONTEND="noninteractive" HOME="/"

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install build-essential and dependencies
RUN \
    apt-get update &&\
    apt-get -y install \
        build-essential pkg-config libssl-dev git bzip2 wget cmake tzdata \
	libavahi-client-dev zlib1g-dev libcurl4-gnutls-dev python \
	liburiparser1 liburiparser-dev gettext \
	libhdhomerun-dev dvb-apps \
	libarchive-zip-perl libdata-dump-perl libdate-manip-perl libdatetime-format-iso8601-perl libdatetime-format-strptime-perl \
	libdatetime-perl libdatetime-timezone-perl libhtml-parser-perl libhtml-tableextract-perl libhtml-tree-perl \
	libhttp-cache-transparent-perl libio-compress-perl libio-stringy-perl libjson-perl libparse-recdescent-perl \
	libsoap-lite-perl libterm-readkey-perl libtext-bidi-perl libtext-iconv-perl libwww-mechanize-perl \
	libwww-perl libxml-dom-perl libxml-libxml-perl libxml-libxslt-perl libxml-parser-perl libxml-twig-perl \
	libxml-writer-perl libxmltv-perl perl perl-modules libxml-treepp-perl liblingua-en-numbers-ordinate-perl

# Compile tvheadend 
RUN \
    cd /tmp &&\
    git clone https://github.com/tvheadend/tvheadend.git &&\
    cd /tmp/tvheadend &&\
    ./configure &&\
    make &&\
    make install
        
#Clean-Up    
RUN \    
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create group "nobody" with groupid 99 (according Host-System)
# Modify userid of user "nobody" to 99 (according Host-System)
# Delete unused User and group irc (free the User-ID and Group-ID 39)
# Set Group video to Group-ID 39 (according Host-System)  
RUN \
    groupadd -g 99 nobody &&\
    usermod -u 99 -g 99 nobody &&\
    userdel irc && \
    groupmod -g 39 video &&\  
    usermod -a -G video nobody 
    
#Setup locale
#Change to your location
RUN \
    locale-gen de_DE.UTF-8 &&\
    locale-gen en_US.UTF-8 &&\
    dpkg-reconfigure locales

#Setup timezone
#Change for your timezone
RUN echo "Europe/Berlin" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

# Add tvheadend to runit
RUN mkdir -p /etc/service/01-tvheadend
ADD tvheadend.sh /etc/service/01-tvheadend/run    
RUN chmod +x /etc/service/01-tvheadend/run

#Ports for tvheadend
EXPOSE 9981 9982

VOLUME \
    /config \ 
    /recordings \ 
    /data \ 
    /logos \
    /timeshift
