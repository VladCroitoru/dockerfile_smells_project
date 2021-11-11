FROM ubuntu:xenial as build

RUN apt update && apt -y install autoconf automake libtool libltdl-dev libao-dev libavahi-compat-libdnssd-dev

RUN mkdir /build
WORKDIR /build
COPY . .
RUN ./autogen.sh
RUN ./configure
RUN make


FROM ubuntu:xenial

RUN apt update && apt -y install avahi-daemon libavahi-compat-libdnssd1 libao4 libpulse0 avahi-utils
RUN ln -s libdns_sd.so.1 /usr/lib/x86_64-linux-gnu/libdns_sd.so
COPY avahi-daemon.conf /etc/avahi/
COPY --from=build /build /build
ENV PULSE_SERVER=pulse
CMD /build/run.sh
