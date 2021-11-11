FROM ubuntu:trusty
MAINTAINER Dario Andrei <wouldgo84@gmail.com>

ENV TERM xterm
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git \
  libtool \
  automake \
  pkg-config \
  libcurl4-gnutls-dev \
  sudo \
  build-essential \
  libboost1.54-all-dev \
  software-properties-common \
  wget

RUN git clone --depth=1 --recurse-submodules --single-branch --branch=master https://github.com/valhalla/mjolnir.git && \
  cd mjolnir && \
  ./scripts/dependencies.sh && \
  ./scripts/install.sh && \
  cd ..

RUN git clone --depth=1 --recurse-submodules --single-branch --branch=master https://github.com/valhalla/tools.git && \
  cd tools && \
  ./scripts/dependencies.sh && \
  ./scripts/install.sh && \
  cd ..

ADD ./conf /conf

RUN ldconfig

RUN wget https://s3.amazonaws.com/metro-extracts.mapzen.com/chicago_illinois.osm.pbf

RUN mkdir -p /data/valhalla
RUN valhalla_build_admins -c conf/valhalla.json *.pbf
RUN valhalla_build_tiles -c conf/valhalla.json *.pbf

RUN apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8002
CMD ["tools/valhalla_route_service", "conf/valhalla.json"]
