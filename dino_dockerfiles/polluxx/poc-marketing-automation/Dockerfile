FROM node:5.10

RUN  mkdir /src && npm install nodemon bower gulp-cli -g && apt-get update && apt-get install -y wget

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

COPY ./ /src
WORKDIR /src
RUN npm install && bower install --allow-root && NODE_ENV=production gulp build

EXPOSE 5000

CMD dockerize -wait http://arangodb:8529 -timeout 60s npm start
