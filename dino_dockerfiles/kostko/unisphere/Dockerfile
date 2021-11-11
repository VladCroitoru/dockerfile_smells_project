FROM ubuntu:trusty
MAINTAINER Jernej Kos, jernej@kos.mx

# Add snapshot of current code
WORKDIR /code
ADD . /code

# Setup environment variable defaults
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
 apt-get install --no-install-recommends -y git python python-dev python-pip build-essential scons wget ca-certificates && \
 cat /code/packages.txt | xargs apt-get --no-install-recommends -y --force-yes install && \
 cd /tmp && \
 wget -O - http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.bz2 | tar xjf - && \
 cd boost_1_55_0 && \
 ./bootstrap.sh --prefix=/usr && \
 ./b2 install && \
 cd /tmp && \
 rm -rf /tmp/boost* && \
 wget -O - https://download.libsodium.org/libsodium/releases/libsodium-1.0.6.tar.gz | tar xzf - && \
 cd libsodium-* && \
 ./configure --prefix=/usr && \
 make && \
 make install && \
 cd /tmp && \
 rm -rf /tmp/libsodium-* && \
 git clone https://github.com/mongodb/mongo-cxx-driver.git /tmp/mongo-cxx-driver && \
 cd /tmp/mongo-cxx-driver && \
 git checkout 5a41685f37ad4c474fc75c9f271e82e37f843b29 && \
 scons --ignore-errors --sharedclient --release --c++11 --prefix /usr install && \
 rm -rf /tmp/mongo-cxx-driver && \
 cd /code && \
 mkdir build && \
 ./tools/bootstrap.sh /usr "-DUNISPHERE_CRYPTO_NOOP=ON" && \
 cd build/release && \
 make

