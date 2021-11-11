FROM node:alpine
MAINTAINER lapwat

ADD src /root/src
WORKDIR /root/src
RUN npm install

EXPOSE 8080
CMD ["npm", "start"]
