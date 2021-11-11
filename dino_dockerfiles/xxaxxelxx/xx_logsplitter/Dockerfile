FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq -y install sudo

RUN apt-get -qq -y install mc 
RUN apt-get -qq -y install less
RUN apt-get -qq -y install bc 
RUN apt-get clean

VOLUME /customer

COPY ./*.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
#CMD [ "bash" ]
