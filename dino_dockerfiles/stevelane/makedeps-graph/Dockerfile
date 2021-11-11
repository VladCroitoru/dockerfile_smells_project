FROM debian:jessie
LABEL maintainer="Steve Lane"
LABEL email="lane.s@unimelb.edu.au"

## Update and install extra packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  g++ \
  graphviz \
  make \
  openssl \
  ttf-freefont \
  wget

## Grab in makefile2graph
RUN cd /tmp \
  && wget --no-check-certificate https://github.com/lindenb/makefile2graph/archive/master.tar.gz \
  && tar -xzf master.tar.gz \
  && cd makefile2graph-master \
  && make && make install

## Create folder for assets and copy over
RUN cd /tmp \
  && mkdir graph

COPY create-graph.sh /tmp

RUN chmod u+x /tmp/create-graph.sh

## Now run makefile2graph on a Makefile in an attached volume
CMD "/tmp/create-graph.sh"
