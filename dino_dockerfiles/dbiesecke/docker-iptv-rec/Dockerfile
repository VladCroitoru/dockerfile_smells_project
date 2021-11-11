#
FROM debian
MAINTAINER dbiesecke

ADD http://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-multimedia-keyring_2015.6.1_all.deb /keyring.deb 
RUN dpkg -i /keyring.deb 
RUN echo 'deb http://www.deb-multimedia.org jessie main non-free' > /etc/apt/sources.list.d/ffmpeg.list 
RUN echo 'deb ftp://ftp.deb-multimedia.org jessie main non-free' >> /etc/apt/sources.list.d/ffmpeg.list 

RUN apt-get update
RUN apt-get install ffmpeg python-setuptools ca-certificates openssl -y -f
RUN easy_install livestreamer 

RUN apt-get install curl psmisc -y -f

WORKDIR /video
ADD run-rip.pl /run.pl
RUN chmod +x /run.pl
ENTRYPOINT ["perl","/run.pl"]

