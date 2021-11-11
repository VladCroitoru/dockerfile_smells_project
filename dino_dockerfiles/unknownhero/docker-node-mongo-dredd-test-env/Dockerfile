FROM node:6.6.0

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 && \
  echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \
  apt-get update && \
  apt-get install -y mongodb-org

#install globals
RUN npm install -g nodemon dredd babel-cli migrate phantomjs node-inspector