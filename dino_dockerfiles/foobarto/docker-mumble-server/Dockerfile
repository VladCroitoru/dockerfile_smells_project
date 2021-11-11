FROM busybox
MAINTAINER  Bartosz Ptaszynski <foobarto@gmail.com>

ENV MUMBLE_VERSION 1.2.11

# Default port for mumble
EXPOSE 64738 64738/udp

RUN mkdir /data 

ADD https://github.com/mumble-voip/mumble/releases/download/$MUMBLE_VERSION/murmur-static_x86-$MUMBLE_VERSION.tar.bz2 /murmur-static_x86-$MUMBLE_VERSION.tar.bz2
RUN tar xvf murmur-static_x86-$MUMBLE_VERSION.tar.bz2 && \
    cp murmur-static_x86-$MUMBLE_VERSION/murmur.x86 /usr/sbin/murmurd && \
    adduser -S -u 1000 mumble-server mumble-server && \
    chown mumble-server /data 

USER mumble-server

ADD ./mumble-server.ini /data/mumble-server.ini
ADD ./start /start
VOLUME ["/data"]

CMD ["/start"]
