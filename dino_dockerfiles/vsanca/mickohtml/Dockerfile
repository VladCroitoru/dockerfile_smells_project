FROM fedora:24
MAINTAINER authext <wolf.srb.ns@hotmail.com>
EXPOSE 80
RUN dnf install -y git cmake make gcc gcc-c++ flex bison nodejs npm
WORKDIR root
RUN git clone https://github.com/vsanca/MickoHTML --depth 1 --branch master
WORKDIR MickoHTML/Micko
RUN cmake -G "Unix Makefiles" .
RUN make
WORKDIR ../MickoView
RUN npm install
ENTRYPOINT ["/usr/bin/node", "/root/MickoHTML/MickoView/server.js", "/root/MickoHTML/Micko/Micko"]

