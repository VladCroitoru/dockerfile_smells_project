FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y u-boot-tools android-tools-fastboot git build-essential \
                       libusb-1.0-0-dev libncurses5-dev libc6-i386 lib32stdc++6 \
                       lib32z1 android-tools-fsutils pkg-config

RUN mkdir chip-files
WORKDIR chip-files

RUN git clone http://github.com/NextThingCo/sunxi-tools
WORKDIR sunxi-tools
RUN make
RUN rm -f /usr/local/bin/fel
RUN ln -s $PWD/fel /usr/local/bin/fel

WORKDIR chip-files
RUN git clone http://github.com/NextThingCo/CHIP-tools 

WORKDIR CHIP-tools

CMD ./chip-update-firmware.sh

