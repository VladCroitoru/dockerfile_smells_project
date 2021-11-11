FROM busybox:ubuntu

ARG VERSION=1.2.11
ADD https://github.com/mumble-voip/mumble/releases/download/${VERSION}/murmur-static_x86-${VERSION}.tar.bz2 /build/

RUN cd /build &&\
    tar -xjvf murmur-static_x86-${VERSION}.tar.bz2 &&\
    cp /build/murmur-static_x86-${VERSION}/murmur.x86 /bin/murmur &&\
    rm -r /build


# Touch murmur.sqlite, so murmur uses /root/murmur.sqlite as
# the database
RUN touch /etc/murmur.sqlite
COPY ./murmur.ini /etc/murmur.ini

VOLUME /root

EXPOSE 64738
CMD mkdir -p /root/murmur ;\
    test ! -e /root/murmur/murmur.ini &&\
    cp /etc/murmur.ini /root/murmur/murmur.ini;\
    /bin/murmur -ini /root/murmur/murmur.ini -fg
