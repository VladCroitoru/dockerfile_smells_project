FROM alpine:3.7

RUN apk --no-cache add glib libev ragel lua zlib libbz2 openssl \
 && apk --no-cache add --virtual build-dependencies gcc g++ glib-dev make libtool automake autoconf libev-dev lua-dev zlib-dev openssl-dev \
 && wget https://git.lighttpd.net/lighttpd/lighttpd2.git/snapshot/lighttpd2-master.tar.gz \
 && tar xfvz lighttpd2-master.tar.gz \
 && cd lighttpd2-master \
 && ./autogen.sh \
 && ./configure --with-lua --with-openssl --with-kerberos5 --with-zlib --with-bzip2 --includedir=/usr/include/lighttpd-2.0.0 \
 && make \
 && make install \
 && cd .. && rm -rf lighttpd2-master* \
 && apk del build-dependencies \
 && adduser -D www-data \
 && mkdir -p /run/fastcgi

COPY ./conf /etc/lighttpd2

WORKDIR /var/www

CMD ["lighttpd2", "-c", "/etc/lighttpd2/angel.conf"] 
