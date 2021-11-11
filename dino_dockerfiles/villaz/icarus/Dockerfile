FROM ubuntu 
MAINTAINER Luis Villazon <villazonpersonal@gmail.com>

RUN apt-get update && apt-get install -y wget gcc g++ python git make avahi-daemon avahi-utils libavahi-compat-libdnssd-dev dbus

WORKDIR /tmp 
RUN wget http://download.zeromq.org/zeromq-4.1.0-rc1.tar.gz 
RUN tar xzvf zeromq-4.1.0-rc1.tar.gz 


WORKDIR /tmp/zeromq-4.1.0 
RUN ./configure; make ; make install

WORKDIR /tmp 
RUN wget http://nodejs.org/dist/v0.10.33/node-v0.10.33.tar.gz 
RUN tar xzvf node-v0.10.33.tar.gz 
WORKDIR /tmp/node-v0.10.33 
RUN ./configure; make; make install

WORKDIR /tmp 
RUN rm -rf node* 
RUN rm -rf zeromq*

RUN npm install -g coffee-script 
RUN npm install -g mocha

WORKDIR / 
RUN git clone https://github.com/Villaz/Icarus.git 

WORKDIR /Icarus 
RUN npm install

RUN mkdir -p /var/run/dbus/
RUN chown messagebus:messagebus /var/run/dbus

CMD dbus-daemon --system; /usr/sbin/avahi-daemon
