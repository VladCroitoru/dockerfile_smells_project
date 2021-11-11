FROM alpine

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" | cat - /etc/apk/repositories  > repositories && mv -f repositories /etc/apk
RUN apk add --no-cache mono mono-dev git bash automake autoconf findutils make pkgconf libtool g++
RUN mkdir /opt
RUN git clone https://github.com/mono/xsp.git /opt/xsp
RUN cd /opt/xsp && ./autogen.sh && ./configure --prefix=/usr && make && make install
RUN rm -rf /opt/xsp
RUN apk del mono-dev git bash automake autoconf findutils make pkgconf libtool g++
