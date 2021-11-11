FROM node

#Setup apt-get for MongoDB:
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

#apt-get:
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y git && apt-get install -y --force-yes mongodb-org && mkdir -p /data/db

#Global npm installs:
RUN npm install -g bower && npm install -g grunt-cli

#Git clone project and setup:
RUN git clone https://github.com/SweatyFigs/SweatyFigs.git
WORKDIR "/SweatyFigs"
RUN cp ./server/env/config_sample.js ./server/env/config.js && echo '{ "allow_root": true }' > /root/.bowerrc

#Install dependencies:
RUN npm install
RUN bower install

#EXPOSE 27017
#ENTRYPOINT ["/usr/bin/mongod"]

#Start daemons:
#RUN mongod --fork --logpath ./mongod.log
#RUN npm start

EXPOSE 8080

