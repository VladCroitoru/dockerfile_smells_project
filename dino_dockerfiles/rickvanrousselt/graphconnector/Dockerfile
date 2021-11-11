# Use latest Ubuntu as the base image
FROM ubuntu:latest

#Add maintainer of this Docker file
MAINTAINER rick@rivaro.be

#Prepare base ubuntu image
RUN apt-get update
RUN apt-get install -y nodejs nodejs-legacy npm
RUN apt-get clean

#First install the required packages
COPY ./package.json src/
RUN cd src && npm install

#Then copy all the source code
COPY . /src

#Set working directory for docker daemon
WORKDIR src/

#Set default comment on start
CMD ["npm","start"]


#docker run -d -p 80:3000 dockergraph