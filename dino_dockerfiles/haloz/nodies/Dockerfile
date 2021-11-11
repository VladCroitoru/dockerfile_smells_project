FROM node:latest
RUN apt-get install -y git git-core
RUN rm -rf /opt/apps/nodies; true
RUN mkdir -p /opt/apps/nodies
WORKDIR /opt/apps/nodies
RUN git clone https://github.com/haloz/nodies.git /opt/apps/nodies
RUN npm install
EXPOSE 20080
CMD node_modules/forever/bin/forever --watch server/server.js

