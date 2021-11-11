FROM ubuntu:17.04

RUN apt update && apt install -yq git cmake build-essential libpng-dev libjpeg-dev ninja-build \
    libfreetype6-dev libglew-dev libreadline-dev libsdl2-dev libqt5widgets5 \
    qtbase5-dev libsdl2-mixer-dev libdw-dev
VOLUME /openclonk
WORKDIR openclonk
ADD build.sh /build.sh

ENTRYPOINT ["/build.sh"]
