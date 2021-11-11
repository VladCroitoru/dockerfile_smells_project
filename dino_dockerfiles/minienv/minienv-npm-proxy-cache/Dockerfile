FROM node:alpine

MAINTAINER Mark Watson <markwatsonatx@gmail.com>

RUN npm install -g npm-proxy-cache

VOLUME /cache

EXPOSE 5001

CMD ["npm-proxy-cache", "-h", "0.0.0.0", "-p", "5001", "-s", "/cache", "-t", "2592000"]
