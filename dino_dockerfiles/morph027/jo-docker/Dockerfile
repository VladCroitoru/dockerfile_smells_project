FROM alpine:3.7 as builder

WORKDIR /tmp

RUN mkdir /tmp/installdir

RUN apk --no-cache add \
      build-base \
      git \
      autoconf \
      automake

RUN git clone git://github.com/jpmens/jo.git

WORKDIR /tmp/jo

RUN autoreconf -i

RUN ./configure

RUN make install DESTDIR=/tmp/installdir

FROM alpine:3.7

COPY --from=builder /tmp/installdir/usr/local/ /usr/local/
