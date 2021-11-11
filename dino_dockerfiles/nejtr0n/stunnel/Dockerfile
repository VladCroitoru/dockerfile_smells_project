FROM debian:jessie
MAINTAINER nejtr0n a6y@xakep.ru
ENV STUNNEL_VERSION 5.32
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get -y install build-essential wget openssl libssl-dev
RUN wget -O - https://www.stunnel.org/downloads/stunnel-$STUNNEL_VERSION.tar.gz | tar -C /usr/local/src -zxv
WORKDIR /usr/local/src/stunnel-$STUNNEL_VERSION
RUN ./configure && make && make install

CMD ["sleep", "100000"]
