FROM node:latest

COPY ./package.json /src/package.json
RUN cd /src && npm install
COPY  ./ /src

WORKDIR /src
#ENV DEBUG=*


CMD ["npm", "start"]
