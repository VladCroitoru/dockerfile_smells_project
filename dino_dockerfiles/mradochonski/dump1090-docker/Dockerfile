FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  git-core \
  cmake \
  libusb-1.0-0-dev \
  build-essential \
  pkg-config \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /
RUN git clone git://git.osmocom.org/rtl-sdr.git
RUN cd rtl-sdr
RUN mkdir build

WORKDIR /rtl-sdr/build
RUN cmake ../ -DINSTALL_UDEV_RULES=ON
RUN make all
RUN make install
RUN ldconfig

WORKDIR /
RUN cp ./rtl-sdr/rtl-sdr.rules /etc/udev/rules.d/

RUN git clone git://github.com/mradochonski/dump1090.git

WORKDIR /dump1090
RUN make

EXPOSE 8080 30001 30002 30003 30004 30005

ENTRYPOINT ./dump1090 --net
