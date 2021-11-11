#Docker file
FROM node:0.10-onbuild
ADD package.json /usr/src/app/
WORKDIR /usr/src/app
RUN npm install mouyigang/zoho-node
RUN npm install request
EXPOSE 8889
