FROM ubuntu:14.04

RUN apt-get -q -y update \
 && apt-get -q -y install git wget curl tar gzip build-essential python-dev \
 && apt-get -q -y install build-essential g++ flex bison gperf ruby perl libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev libpng-dev libjpeg-dev \
 && apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# node
RUN wget -O - http://nodejs.org/dist/v0.10.23/node-v0.10.23.tar.gz | tar xvzf - && \
    cd node-v0.10.23 && ./configure --prefix=/usr && make && make install 

RUN npm install -g grunt-cli gulp

# phantomjs
RUN wget https://github.com/Pyppe/phantomjs2.0-ubuntu14.04x64/raw/master/bin/phantomjs && \
  chmod +x phantomjs && mv phantomjs /usr/local/bin
  
