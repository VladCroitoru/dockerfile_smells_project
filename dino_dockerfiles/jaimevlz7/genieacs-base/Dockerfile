FROM node:8.11

MAINTAINER LUXNETWORK Engineering <eng@luxnetwork.lu>

# Download GenieACS
RUN cd /opt && git clone https://github.com/zaidka/genieacs.git

# Setup GenieACS
WORKDIR /opt/genieacs
RUN npm install && npm run configure && npm run compile
COPY config.json config/config.json
