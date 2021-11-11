FROM ubuntu:14.04
ENV BUILD_PACKAGES "xsltproc libxerces-c-dev xsdcxx libboost1.55-dev libboost-filesystem1.55-dev libboost-system1.55-dev cmake g++ git"
ENV RUNTIME_PACKAGES "libxerces-c3.1 libboost-filesystem1.55.0 libboost-system1.55.0"
RUN apt-get -y -qq update \
&&  apt-get -y --fix-missing install $BUILD_PACKAGES \
&&  git clone https://github.com/IGNF/lidarformat.git \
&&  cd lidarformat \
&&  mkdir build \
&&  cd build \
&&  cmake -DBUILD_TESTS=OFF  -DCMAKE_BUILD_TYPE=Release .. \
&&  make install \
&&  rm -rf lidarformat \
&&  AUTO_ADDED_PACKAGES=`apt-mark showauto` \
&&  apt-get remove --purge -y $BUILD_PACKAGES $AUTO_ADDED_PACKAGES \
&&  apt-get -y --fix-missing install $RUNTIME_PACKAGES \
&&  apt-get -y clean \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
