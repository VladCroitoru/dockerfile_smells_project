FROM phusion/baseimage:latest 
WORKDIR /home/ 
RUN /usr/sbin/enable_insecure_key
RUN apt-get update -y
RUN apt-get install nodejs nano git npm screen build-essential -y
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install colors express@3.4.8 
RUN npm install -g nodemon  express@3.4.8
