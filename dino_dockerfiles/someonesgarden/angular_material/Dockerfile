FROM node:argon

MAINTAINER 0.1 Daisuke Nishimura d@someonesgarden.org

RUN groupadd -r express && useradd -r -g express express

#apt-get
RUN apt-get update && \
apt-get install -y \
vim \
git

#Create app directory
# Install app dependencies
RUN mkdir -p /usr/src/app
COPY package.json /usr/src/app/

WORKDIR /usr/src/app
RUN npm install && npm update -g
RUN npm install -g bower grunt-cli coffee-script && \
echo '{ "allow_root": true }' > /root/.bowerrc

WORKDIR /usr/src/app/public
RUN bower install backbone underscore jquery  --save
RUN bower install glyphicons glyphicons-halflings --save
RUN bower install bootstrap --save
RUN bower install angular angular-material \
angular-messages angular-route \
angular-resource angular-sanitize \
angular-local-storage --save
RUN bower install d3 --save

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8080

#CMD [ "npm", "start" ]
CMD [ "coffee", "bin/www.coffee" ]


