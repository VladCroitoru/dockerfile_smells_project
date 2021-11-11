FROM debian:wheezy
MAINTAINER bohms@msu.edu

RUN apt-get clean;apt-get update;apt-get -y upgrade

ADD setup.sh /
RUN sh /setup.sh

#RUN git clone https://github.com/kf8a/aglog.git
#RUN cd /aglog;bundle
