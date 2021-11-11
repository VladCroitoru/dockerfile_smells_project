FROM node:latest
MAINTAINER Alexander Y Lyapko sunsay@maprox.net
RUN mkdir -p /opt/stratum-reader
COPY . /opt/stratum-reader
WORKDIR /opt/stratum-reader
RUN npm install
CMD [ "npm", "start" ]