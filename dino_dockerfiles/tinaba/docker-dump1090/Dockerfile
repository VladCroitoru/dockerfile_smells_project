FROM ubuntu:16.04
MAINTAINER Takashi Inaba

RUN apt-get update && \
    apt-get install -y libusb-1.0-0-dev pkg-config ca-certificates git-core cmake build-essential module-init-tools libbladerf-dev libpcap-dev libncurses5-dev --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN echo 'blacklist dvb_usb_rtl28xxu' > /etc/modprobe.d/raspi-blacklist.conf && \
    git clone git://git.osmocom.org/rtl-sdr.git && \
    mkdir rtl-sdr/build && \
    cd rtl-sdr/build && \
    cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON && \
    make && \
    make install && \
    ldconfig && \
    rm -rf /tmp/rtl-sdr

WORKDIR /tmp 

RUN git clone https://github.com/flightaware/dump1090.git

WORKDIR /tmp/dump1090

RUN make

ENTRYPOINT ["./dump1090"]
