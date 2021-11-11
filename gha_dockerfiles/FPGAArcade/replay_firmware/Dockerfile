# $ docker build -t replay_fw_tools .
# $ docker run --volume "$PWD":/host --workdir /host -i -t replay_fw_tools

FROM ubuntu:20.10

RUN apt-get update                                              && \
    apt-get install -y make git curl                            && \
    apt-get install -y gcc-arm-none-eabi                        && \
    apt-get remove -y libnewlib-dev                             && \
    apt-get remove -y libnewlib-arm-none-eabi                   && \
    apt-get remove -y libstdc++-arm-none-eabi-newlib            && \
    apt-get install -y gcc g++ gdb libncurses-dev               && \
    apt-get install -y zip libarchive-zip-perl                  && \
    apt-get install -y dosfstools mtools valgrind               && \
    apt-get install -y screen socat                             && \
    apt-get clean

ARG REPO=https://github.com/FPGAArcade/replay_firmware.git
RUN cd /root                                                   && \
    git clone --depth 1 $REPO                                  && \
    ./replay_firmware/Replay_Boot/install_arduino_vidor.sh     && \
    rm -rf replay_firmware

ENV ARDUINO_ROOT=/root/.arduino
