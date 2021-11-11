FROM debian:jessie
MAINTAINER xxaxxelxx <x@axxel.net>

RUN sed -e 's/$/ contrib non-free/' -i /etc/apt/sources.list 

RUN apt-get -qq -y update
#RUN apt-get -qq -y dist-upgrade

ENV DEBIAN_FRONTEND=noninteractive

RUN groupadd liquidsoap
RUN useradd -g liquidsoap -m liquidsoap
RUN apt-get -qq -y install wget
RUN apt-get -qq -y install sudo
RUN apt-get -qq -y install g++
RUN apt-get -qq -y install make
RUN apt-get -qq -y install libcamomile-ocaml-dev
RUN apt-get -qq -y install libtaglib-ocaml
RUN apt-get -qq -y install libavutil-dev
RUN apt-get -qq -y install libswscale-dev
RUN apt-get -qq -y install libpcre-ocaml-dev
RUN apt-get -qq -y install libao-dev
RUN apt-get -qq -y install libmad0-dev
RUN apt-get -qq -y install libtag1-dev
RUN apt-get -qq -y install libmp3lame-dev
RUN apt-get -qq -y install libogg-dev
RUN apt-get -qq -y install libvorbis-dev
RUN apt-get -qq -y install libopus-dev
RUN apt-get -qq -y install libfdk-aac-dev 

ADD liquidsoap-1.1.1-full.tar.gz /usr/local/liquidsoap
COPY PACKAGES /usr/local/liquidsoap/liquidsoap-1.1.1-full/PACKAGES
WORKDIR /usr/local/liquidsoap/liquidsoap-1.1.1-full


RUN sudo -u liquidsoap ./configure
RUN make
RUN make install

WORKDIR /

RUN mkdir -p /var/log/liquidsoap
RUN chown -R liquidsoap /var/log/liquidsoap
RUN mkdir -p /etc/liquidsoap

# clean up
RUN apt-get clean

COPY *.liq /etc/liquidsoap/
#COPY bbradio.liq /etc/liquidsoap/bbradio.liq
#COPY bbradio-ch.liq /etc/liquidsoap/bbradio-ch.liq
#COPY radioteddy.liq /etc/liquidsoap/radioteddy.liq
#COPY radioteddy-ch.liq /etc/liquidsoap/radioteddy-ch.liq
#COPY ostseewelle.liq /etc/liquidsoap/ostseewelle.liq
#COPY ostseewelle-ch.liq /etc/liquidsoap/ostseewelle-ch.liq

RUN chown -R liquidsoap:liquidsoap /etc/liquidsoap
RUN chmod 600  /etc/liquidsoap/*.liq

COPY ./entrypoint.sh /entrypoint.sh
RUN chown liquidsoap:liquidsoap /entrypoint.sh
RUN chmod 700 /entrypoint.sh

USER liquidsoap:liquidsoap

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "bash" ]
