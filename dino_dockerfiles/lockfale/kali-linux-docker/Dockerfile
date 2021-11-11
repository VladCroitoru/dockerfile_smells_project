# Docker container for running kali tools without need for a whole VM on Linux
#
# Use Kali the latest Kali Linux base image
FROM kalilinux/kali-linux-docker
MAINTAINER David Mitchell "david.mitchell@digital-shokunin.net"

#Expose port for remote shells or whatever
EXPOSE 443

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
RUN apt-get -y update && apt-get -y dist-upgrade && apt -y autoremove && apt-get clean 

#Add source repo after updating keys etc
RUN echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get -y dist-upgrade && apt -y autoremove && apt clean

CMD ["/bin/bash"]
