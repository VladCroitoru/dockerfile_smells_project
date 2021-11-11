FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

#RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq -y install mc
RUN apt-get -qq -y install curl
RUN apt-get -qq -y install rrdtool
RUN apt-get -qq -y install libxml2-utils

# clean up
RUN apt-get clean

COPY *.sh /
RUN chmod 700 /*.sh

ENV RRD_LOOP=300

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
#CMD [ "bash" ]
