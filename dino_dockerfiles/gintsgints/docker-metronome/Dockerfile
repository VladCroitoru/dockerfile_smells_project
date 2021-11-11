# docker-metronome
#
# VERSION 0.1

FROM ubuntu:xenial
MAINTAINER Gints Polis <polis.gints@gmail.com>

# Image maintenance
RUN apt-get update

# Development tools
RUN apt-get install -y build-essential
RUN apt-get install -y dh-autoreconf
RUN apt-get install -y autoconf
RUN apt-get install -y libeigen3-dev
RUN apt-get install -y libboost-all-dev
RUN apt-get install -y git
RUN apt-get install -y supervisor

# Metronome compile
RUN git clone https://github.com/gintsgints/metronome.git /metronome
RUN cd /metronome \
    && ./bootstrap \
    && ./configure \
    && make

# Prepeare run enviroment
RUN mkdir /stats
ADD ./assets/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# webservice, carbon ports
EXPOSE 8000
EXPOSE 2003

CMD /usr/bin/supervisord