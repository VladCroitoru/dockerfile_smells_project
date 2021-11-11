FROM alpine:3.3

RUN apk add --no-cache --virtual=build-dependencies \
  git\
  cmake\
  build-base

RUN apk add --no-cache \
  libusb-dev\
  bash\
  python3

WORKDIR /tmp

RUN git clone git://git.osmocom.org/rtl-sdr.git && \
    mkdir rtl-sdr/build && \
    cd rtl-sdr/build && \
    cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON && \
    make  && \
    make install

RUN git clone https://github.com/merbanan/rtl_433.git && \
    cd rtl_433 && \
    git reset --hard $commit_id && \
    mkdir build && \
    cd build && \
    cmake ../ && \
    make && \
    make install

RUN apk del --purge build-dependencies

RUN rm -rf /tmp
RUN rm -rf /var/cache/apk/*
