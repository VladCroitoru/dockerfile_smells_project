FROM node:4.4.5
MAINTAINER tomo3110 <uotias64_mole@yahoo,co.jp> (https://github.com/tomo3110/minutes-sync-standalone.git)
RUN git clone --depth 1 https://github.com/tomo3110/minutes-sync-standalone.git
WORKDIR minutes-sync-standalone
ENV PORT=3110
RUN npm install
CMD npm start
