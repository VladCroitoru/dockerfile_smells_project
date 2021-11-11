# docker build -t mapbox-docker .
# docker run mapbox-docker
# docker run -it -v $PWD:/root/:Z --rm --entrypoint sh mapbox-docker

FROM ubuntu:14.04
ENTRYPOINT sh -c "echo Hello Mapbox"

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update

RUN add-apt-repository --yes ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN apt-get install -y gcc-5 g++-5

ENV _CXX=g++-5
ENV _CC=gcc-5
ENV CXX=g++-5
ENV CC=gcc-5

RUN apt-get install -y software-properties-common
RUN add-apt-repository --yes ppa:george-edison55/cmake-3.x
RUN apt-get update

RUN apt-get -yq --no-install-suggests --no-install-recommends --force-yes install cmake cmake-data

RUN sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5

RUN apt-get install -y curl git build-essential zlib1g-dev automake \
                     libtool xutils-dev make cmake pkg-config python-pip \
                     libcurl4-openssl-dev libpng-dev libsqlite3-dev \
                     libllvm3.4

RUN apt-get install -y libxi-dev libglu1-mesa-dev x11proto-randr-dev \
                     x11proto-xext-dev libxrandr-dev \
                     x11proto-xf86vidmode-dev libxxf86vm-dev \
                     libxcursor-dev libxinerama-dev

#ENV MAPBOX_ACCESS_TOKEN=""
#ENV MAPBOX_STYLE_URL=""

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs
