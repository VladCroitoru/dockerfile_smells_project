FROM ubuntu:15.04

MAINTAINER Andy McGrath (apextc)

#Update uBuntu and install apps needed for build
RUN apt-get update
RUN apt-get install -y wget unzip

#Node system setup, download and install
RUN mkdir _node
RUN cd $_
RUN wget http://nodejs.org/dist/v0.10.38/node-v0.10.38-linux-x64.tar.gz -O - | tar zxf - --strip-components=1
RUN cp -r ./lib/node_modules/ /usr/local/lib/
RUN cp -r ./include/node /usr/local/include/
RUN mkdir /usr/local/man/man1
RUN cp ./share/man/man1/node.1 /usr/local/man/man1/
RUN cp bin/node /usr/local/bin/
RUN ln -s "/usr/local/lib/node_modules/npm/bin/npm-cli.js" ../npm
RUN npm install npm -g

#Ghost system setup, download
RUN mkdir /var/www
RUN wget -O /var/www/ghost.zip https://ghost.org/zip/ghost-latest.zip
RUN unzip -uo /var/www/ghost.zip -d /var/www/ghost

#Add Ghost configuration file
ADD config.js /var/www/ghost/config.js

#Ghost install
RUN cd /var/www/ghost/ && npm install --production

#System clean-up
RUN rm -f /usr/local/node-*.tar.gz /var/www/ghost.zip
RUN apt-get -y remove unzip wget
RUN apt-get autoclean
RUN apt-get clean

#Set default port (use -P in docker run command)
EXPOSE 2368

#Set default run docker run command string
CMD cd /var/www/ghost/ && npm start --production
