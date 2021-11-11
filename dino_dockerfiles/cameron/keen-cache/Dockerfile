from debian:wheezy

RUN echo deb http://nginx.org/packages/debian/ wheezy nginx >>/etc/apt/sources.list

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install make gcc

RUN apt-get -y install wget git python g++ checkinstall
RUN mkdir -p /tmp/nodebuild && wget -N http://nodejs.org/dist/node-latest.tar.gz -O /tmp/nodebuild/node.tgz
RUN tar xzvf /tmp/nodebuild/node.tgz -C /tmp/nodebuild
RUN cd /tmp/nodebuild/node-* && chmod +x configure && ./configure
RUN cd /tmp/nodebuild/node-* && checkinstall -y --install=no --pkgversion 0.11.11 make -j$(($(nproc)+1)) install
RUN dpkg -i /tmp/nodebuild/node-*/node_*

ADD package.json /src/
WORKDIR /src
RUN npm install

ADD . /src

EXPOSE 80

CMD node keen-proxy.js