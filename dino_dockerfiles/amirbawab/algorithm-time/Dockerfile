FROM node:argon
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" >> /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update
RUN apt-get install -y mongodb-org=3.2.8 mongodb-org-server=3.2.8 mongodb-org-shell=3.2.8 mongodb-org-mongos=3.2.8 mongodb-org-tools=3.2.8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN npm install
EXPOSE 3000
RUN echo "/etc/init.d/mongod start; echo 'Speeing 5 seconds to start mongodb server...';sleep 5; npm start" > start.sh
RUN chmod a+x "start.sh"
CMD [ "/bin/bash", "start.sh" ]
