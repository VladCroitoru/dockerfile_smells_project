FROM node:8.6.0

RUN apt-get update \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 \	
  && echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list \
  && apt-get update \
  && apt-get install -y mongodb-org \
  && npm install -g yarn \
  && npm install -g pm2
