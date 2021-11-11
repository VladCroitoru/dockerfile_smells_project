FROM debian:jessie

RUN apt-get update
RUN apt-get install -y build-essential python quilt devscripts python-setuptools python3 libssl-dev cmake libc-ares-dev uuid-dev daemon wget

RUN wget -O libwebsockets.tar.gz https://libwebsockets.org/git/libwebsockets/snapshot/libwebsockets-1.4-chrome43-firefox-36.tar.gz
RUN tar zxvf libwebsockets.tar.gz && cd libwebsockets-1.4-chrome43-firefox-36 && mkdir build && cd build && cmake ..  && make install && ldconfig
RUN wget http://mosquitto.org/files/source/mosquitto-1.4.2.tar.gz && tar zxvf mosquitto-1.4.2.tar.gz && cd mosquitto-1.4.2 && sed -i.bak 's/WITH_WEBSOCKETS:=no/WITH_WEBSOCKETS:=yes/' config.mk && make && make install

RUN adduser mosquitto

ADD mosquitto.conf /etc/mosquitto/mosquitto.conf

EXPOSE 1883
EXPOSE 1884

CMD ["mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
