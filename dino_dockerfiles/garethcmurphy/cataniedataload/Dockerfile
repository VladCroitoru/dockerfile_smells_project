FROM node:9
LABEL maintainer="garethcmurphy@gmail.com"
EXPOSE 8888

WORKDIR /home/node/app
COPY package.json /home/node/app


RUN npm install -g yarn
RUN git clone https://github.com/datacurationproject/CatanieDataLoad.git
WORKDIR /home/node/app/CatanieDataLoad
RUN yarn install
RUN ls
#RUN yarn run mocha -r ts-node/register test/*.ts --exit
#CMD yarn run send
