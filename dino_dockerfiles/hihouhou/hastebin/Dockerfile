#
# Openvpn server Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

# Update & install packages
RUN apt-get update && \
    apt-get install -y git python make build-essential
#    apt-get install -y g++ curl libssl-dev apache2-utils git-core redis-server python make

# install node.js
RUN git clone https://github.com/nodejs/node.git && \
cd node && \
./configure && \
make && \
make install

# install haste-server
#RUN git clone git://github.com/seejohnrun/haste-server.git && \
#cd haste-server && \
#npm install
#npm install hiredis && \ #optional
#npm start

#EXPOSE 7777

#CMD ["redis-server", "/etc/redis/redis.conf"]
#CMD ['npm', 'start']

RUN apt-cache search node | grep js
RUN git clone https://github.com/seejohnrun/haste-server.git haste-server
WORKDIR /haste-server
RUN pwd
RUN npm install

ADD config.js /haste-server/config.js

EXPOSE 7777
CMD ["npm", "start"]

