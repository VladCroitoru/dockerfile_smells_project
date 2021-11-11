FROM node:12-buster

LABEL maintainer="Lynckia"

WORKDIR /opt

#Configure tzdata
ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Download latest version of the code and install dependencies
RUN  apt update && apt install -y git wget curl dos2unix

COPY .nvmrc package.json /opt/licode/

COPY scripts/installUbuntuDeps.sh scripts/checkNvm.sh scripts/libnice-014.patch0 /opt/licode/scripts/

WORKDIR /opt/licode/build/libdeps

# fixing Windows's Corrupted CRLF incase started from docker-desktop-windows
RUN find ../../scripts -type f -exec dos2unix {} \;

# creating prefix_dir
RUN mkdir ./build

# Installing apt deps
RUN npm install --prefix=../..
RUN apt install -qq python3-software-properties software-properties-common -y

ENV GCC_VERSION=7

RUN apt install make gcc-${GCC_VERSION} g++-${GCC_VERSION} python3-pip libssl-dev cmake pkg-config rabbitmq-server curl autoconf libtool automake -y
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-${GCC_VERSION} 60 --slave /usr/bin/g++ g++ /usr/bin/g++-${GCC_VERSION}
RUN chown -R `whoami` ~/.npm ~/tmp/ || true

# installing mongodb
RUN apt install -y libcurl4 openssl liblzma5\
  && wget -P . https://fastdl.mongodb.org/linux/mongodb-shell-linux-x86_64-debian10-4.4.9.tgz\
  && tar -zxvf ./mongodb-shell-linux-x86_64-debian10-4.4.9.tgz -C ./\
  && cp ./mongodb-linux-x86_64-debian10-4.4.9/bin/mongo /usr/local/bin/

# installing conan
RUN pip3 install conan==1.40.4


# download & installing OpenSSL
ENV OPENSSL_VERSION="1.1.1l"
ENV PREFIX_DIR=/opt/licode/build/libdeps/build

RUN curl -OL https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz\
  && tar -zxvf openssl-$OPENSSL_VERSION.tar.gz\
  && cd openssl-$OPENSSL_VERSION\
  && ./config --prefix=${PREFIX_DIR} --openssldir=${PREFIX_DIR} -fPIC\
  && make -j4 -s V=0 && make install_sw

# install libsrtp
RUN curl -o libsrtp-2.4.2.tar.gz https://codeload.github.com/cisco/libsrtp/tar.gz/v2.4.2\
  && tar -zxvf libsrtp-2.4.2.tar.gz && cd libsrtp-2.4.2\
  && CFLAGS="-fPIC" ./configure --enable-openssl --prefix=${PREFIX_DIR} --with-openssl-dir=${PREFIX_DIR}\
  && make -j4 -s V=0 && make uninstall && make install

# download && install opus
RUN curl -L https://github.com/xiph/opus/archive/v1.1.tar.gz -o opus-1.1.tar.gz\
  && tar -zxvf opus-1.1.tar.gz && cd opus-1.1 && ./autogen.sh\
  && ./configure --prefix=${PREFIX_DIR} && make -j4 -s V=0 && make install

# installing cpplint
RUN pip3 install cpplint==1.5.4

# install mediadeps_nogpl
RUN apt -qq install yasm libvpx-dev -y
RUN curl -O -L https://github.com/libav/libav/archive/v11.11.tar.gz\
  && tar -zxvf v11.11.tar.gz && cd libav-11.11\
  && PKG_CONFIG_PATH=${PREFIX_DIR}/lib/pkgconfig ./configure --prefix=${PREFIX_DIR} --enable-shared --enable-libvpx --enable-libopus --disable-doc\
  && make -j4 -s V=0 && make install

# cleanup build files
RUN rm -r libsrtp* &&\
  rm -r libav* &&\
  rm -r v11* &&\
  rm -r openssl* &&\
  rm -r opus* &&\
  rm -r mongodb*.tgz &&\
  rm -r mongodb*


WORKDIR /opt

COPY . /opt/licode

RUN find ./licode -type f -exec dos2unix {} \;

RUN mkdir /opt/licode/.git

# Clone and install licode
WORKDIR /opt/licode/scripts

# running again because scripts changed after copying/cloning
RUN find . -type f -exec dos2unix {} \;

RUN ./installErizo.sh -dfEAcs 
RUN ./../nuve/installNuve.sh 
RUN ./installBasicExample.sh

RUN ldconfig /opt/licode/build/libdeps/build/lib

WORKDIR /opt/licode

ARG COMMIT

RUN echo $COMMIT > RELEASE
RUN date --rfc-3339='seconds' >> RELEASE
RUN cat RELEASE

WORKDIR /opt

ENTRYPOINT ["./licode/extras/docker/initDockerLicode.sh"]