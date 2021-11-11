# start from bitnami apache
FROM bitnami/apache

# Install Node.js, npm and ruby
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y nodejs && ln -s `which nodejs` /usr/bin/node
RUN apt-get install -y npm
RUN apt-get install -y ruby-full 


# install npm basic dependencies
RUN npm install -g yo
RUN npm install -g grunt
RUN npm install -g grunt-cli
RUN npm install -g bower
RUN gem install sass
RUN npm install -g generator-angular-fullstack
