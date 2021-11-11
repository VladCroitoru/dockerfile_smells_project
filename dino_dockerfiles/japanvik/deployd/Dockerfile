FROM japanvik/nodejs
MAINTAINER Vik Kumar "vik@japanvik.net"

#Update npm
RUN sudo apt-get install -y build-essential
RUN npm update
# make directories and setup deployd
RUN mkdir -p /app/src
RUN npm install -g deployd
WORKDIR /app/src
RUN dpd create deployd
WORKDIR /app/src/deployd
RUN dpd keygen
RUN dpd showkey
# Run the daemon
CMD dpd -H ${MONGO_PORT_27017_TCP_ADDR} -P ${MONGO_PORT_27017_TCP_PORT} -d -n deployd
