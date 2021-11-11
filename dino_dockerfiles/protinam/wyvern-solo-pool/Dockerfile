FROM ubuntu:16.04

RUN apt-get update && apt-get -y install git python2.7 build-essential libssl-dev

WORKDIR /

ADD node-v0.10.41.tar.gz /

RUN ln -s /usr/bin/python2.7 /usr/bin/python && cd node-v0.10.41 && ls && ./configure && make && make install

RUN npm install request bunyan && git clone https://github.com/zone117x/node-stratum-pool.git node_modules/stratum-pool && cd /node_modules/stratum-pool && npm update

ADD pool.js /
ADD run.sh  /

CMD ["/run.sh"]
