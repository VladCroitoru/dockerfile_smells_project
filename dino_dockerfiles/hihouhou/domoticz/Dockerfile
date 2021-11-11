#
# Domoticz Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV DOMOTICZ_VERSION 2021.1

# Update & install packages
RUN apt-get update && \
    apt-get install -y python3-dev wget git libssl-dev build-essential libboost-dev libboost-thread-dev libboost-system-dev libsqlite3-dev curl libcurl4-openssl-dev libusb-dev zlib1g-dev 

# Fetch cmake up to date version
RUN wget https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4-Linux-x86_64.sh && \
    bash cmake-3.14.4-Linux-x86_64.sh --skip-license
# Download & deploy domoticz
RUN git clone --branch ${DOMOTICZ_VERSION} https://github.com/domoticz/domoticz.git && \
    cd domoticz && \
    cmake -DCMAKE_BUILD_TYPE=Release CMakeLists.txt -DUSE_OPENSSL_STATIC="NO" && \
    make -j 3

EXPOSE 8080

CMD ["/domoticz/domoticz", "-www 8080"]
