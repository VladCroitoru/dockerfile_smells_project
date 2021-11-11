# VERSION 1.0.0
FROM radektomasek/keboola-base-node-build-tools
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /tmp

# Configure lftp environment.
RUN curl -O http://lftp.yar.ru/ftp/lftp-4.8.4.tar.gz && tar xzvf lftp-4.8.4.tar.gz && cd lftp-4.8.4 && ./configure --with-gnutls --without-openssl --prefix=${HOME}/local && make && make install && mkdir ~/.lftp/ && echo "set ftp:ssl-force true;set ftp:ssl-protect-data true;set ftp:ssl-allow true;set ssl:verify-certificate no;" >> ~/.lftp/rc && ln -s ~/local/bin/lftp /usr/bin/lftp
