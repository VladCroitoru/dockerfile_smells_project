FROM ubuntu:14.04

RUN \
  apt-get update && apt-get install -y \
  wget build-essential git cmake pkg-config \
  libbz2-dev libstxxl-dev libstxxl-doc libstxxl1 libxml2-dev \
  libzip-dev libboost-all-dev lua5.1 liblua5.1-0-dev libluabind-dev libtbb-dev

RUN \
  git clone git://github.com/Project-OSRM/osrm-backend.git /src && \
  cd /src && git checkout v4.9.1 && cd ~ && \
  mkdir -p /build && \
  cd /build && \
  cmake /src && make && \
  mv /src/profiles/car.lua profile.lua && \
  mv /src/profiles/lib/ lib && \
  echo "disk=/tmp/stxxl,25000,syscall" > /build/.stxxl && \
  rm -rf /src

WORKDIR /build
ADD run.sh run.sh
EXPOSE 5000
CMD bash run.sh
