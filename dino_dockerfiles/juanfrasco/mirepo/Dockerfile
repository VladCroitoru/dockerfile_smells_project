FROM library/debian:wheezy
MAINTAINER Juan <jgonz@kk.mail>
## Minimal changes to httpd
#RUN  echo "nameserver 10.27.100.2" > /etc/resolv.conf
RUN apt-get update && \
 apt-get -y upgrade && \
apt-get install -y iputils-ping netcat-traditional && \
apt-get clean && apt-get autoclean && \
rm -rf /var/lib/apt/lists/*
VOLUME ["/miVolum1"]
#RUN apt-get install -y mplayer
#ENTRYPOINT ["mplayer","/miVolum1/frank.mp3"]

