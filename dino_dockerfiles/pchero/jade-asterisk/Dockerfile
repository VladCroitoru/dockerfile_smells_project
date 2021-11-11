FROM debian:9

MAINTAINER Sungtae Kim <pchero@gmail.com>


## Get all asterisk prerequsites 
RUN apt update
RUN apt install -y \
  build-essential \
  openssl \
  libxml2-dev \
  libncurses5-dev \
  uuid-dev \
  sqlite3 \
  libsqlite3-dev \
  pkg-config \
  curl \
  libjansson-dev \
  libssl-dev \
  vim \
  less \
  libopus-dev \
  opus-tools \
  xmlstarlet \
  libsrtp0 \
  libsrtp0-dev \
  git \
  cmake \
  libevent-dev \
  libjansson-dev \
  libbsd-dev \
  libzmq5-dev \
  libonig-dev \
  zlib1g-dev \
  syslog-ng

# Run syslog
RUN /etc/init.d/syslog-ng restart

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt update
RUN apt install -y nodejs
RUN npm install -g @angular/cli

RUN mkdir -p /opt/src
RUN mkdir -p /opt/bin
RUN mkdir -p /opt/var
RUN mkdir -p /opt/etc

# Install other libraries

# Create temp certificate
WORKDIR /opt/etc
RUN openssl req -subj '/CN=US/O=Jade project/C=US' -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt
RUN cat server.key server.crt > jade.pem


# Insall libevhtp
RUN mkdir -p /opt/src/libevhtp
RUN curl -s https://codeload.github.com/criticalstack/libevhtp/tar.gz/1.2.16 | tar xz -C /opt/src/libevhtp --strip-components=1
WORKDIR /opt/src/libevhtp/build
RUN cmake ..
RUN make
RUN make install


# Install libwebsockets
RUN mkdir -p /opt/src/libwebsockets
RUN curl -s https://codeload.github.com/warmcat/libwebsockets/tar.gz/v2.4.2 | tar xz -C /opt/src/libwebsockets --strip-components=1
WORKDIR /opt/src/libwebsockets/build
RUN cmake -DLWS_WITH_LIBEVENT=1 ../
RUN make
RUN make install


## Download and decompress asterisk 15
RUN mkdir -p /opt/src/asterisk
RUN curl -s http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-15-current.tar.gz | tar xz -C /opt/src/asterisk --strip-components=1


## Asterisk compilation & installation
WORKDIR /opt/src/asterisk
RUN ./configure
RUN make menuselect.makeopts

# enable opus codec module
RUN menuselect/menuselect --enable codec_opus --disable chan_sip menuselect.makeopts

# make & make install
RUN make
RUN make install
RUN make samples


# Setting ami user
RUN printf "[general]\nenabled = yes\nport = 5038\nbindaddr = 0.0.0.0\n\n[admin]\nsecret = admin\ndeny = 0.0.0.0/0.0.0.0\npermit = 127.0.0.1/255.255.255.0\nread = all\nwrite = all" > /etc/asterisk/manager.conf
# Setting http
RUN printf "[general]\nservername=Asterisk\nenabled=yes\nbindaddr=0.0.0.0\nbindport=8088\ntlsenable=yes\ntlsbindaddr=0.0.0.0:8089\ntlscertfile=/opt/etc/jade.pem" > /etc/asterisk/http.conf


## Run Asterisk
#CMD ["/usr/sbin/asterisk", "-fvvvvvvv", "&"]


## jade
RUN git clone https://github.com/pchero/jade.git /opt/src/jade
WORKDIR /opt/src/jade/src
RUN make
RUN mv build/jade_backend /opt/bin
RUN ln -s /opt/etc/jade.pem /opt/bin/jade.pem



## jade-me
RUN git clone https://github.com/pchero/jade-me.git /opt/src/jade-me
WORKDIR /opt/src/jade-me
RUN npm install --quiet
RUN ln -s /opt/etc/jade.pem /opt/src/jade-me/jade-me.pem


## jade-admin
RUN git clone https://github.com/pchero/jade-admin.git /opt/src/jade-admin
WORKDIR /opt/src/jade-admin
RUN npm install --quiet
RUN ln -s /opt/etc/jade.pem /opt/src/jade-admin/jade-admin.pem


## jade-manager
RUN git clone https://github.com/pchero/jade-manager.git /opt/src/jade-manager
WORKDIR /opt/src/jade-manager
RUN npm install --quiet
RUN ln -s /opt/etc/jade.pem /opt/src/jade-manager/jade-manager.pem


## Start script
RUN printf "#!/bin/bash -x\necho \"Starting script\"\n/usr/sbin/asterisk -fvvvvvvv &\nsleep 30\n/opt/bin/jade_backend &\ncd /opt/src/jade-manager\nnpm start &\ncd /opt/src/jade-admin\nnpm start &\ncd /opt/src/jade-me\nnpm start &\nwait\necho \"Complete\"" > /opt/bin/start.sh
CMD sh /opt/bin/start.sh




