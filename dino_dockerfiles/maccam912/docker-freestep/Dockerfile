FROM ubuntu
MAINTAINER Matt Koski <maccam912@gmail.com>

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git python build-essential wget screen tmux curl vim mongodb-org -y
RUN sudo service mongod start

RUN mkdir /data
RUN mkdir /data/db

RUN mkdir /Development
RUN cd /Development && git clone git://github.com/joyent/node

RUN cd /Development/node && ./configure && make && make install
RUN rm -rf /Development/node
RUN chmod 777 -R /Development

RUN npm install -g bower grunt-cli

# RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

RUN cd /Development && git clone https://github.com/maccam912/FreeStep.git

RUN mkdir /Development/FreeStep/ssl/
RUN openssl genrsa -out /Development/FreeStep/ssl/server.key 1024
RUN openssl req -new -key /Development/FreeStep/ssl/server.key -out /Development/FreeStep/ssl/freestep_net.csr -subj "/C=US/ST=WI/L=Wausau/O=freestep/OU=IT Department/CN=libertymutual.pw"
RUN yes . | openssl x509 -req -days 365 -in /Development/FreeStep/ssl/freestep_net.csr -signkey /Development/FreeStep/ssl/server.key -out /Development/FreeStep/ssl/freestep_net.crt
RUN cat Development/FreeStep/ssl/freestep_net.crt > /Development/FreeStep/ssl/COMODO.ca-bundle

RUN cd /Development/FreeStep && npm install
RUN cd /Development/FreeStep && bower --allow-root install
CMD ["cd /Development/FreeStep","sudo npm start"]

EXPOSE 80:80
EXPOSE 443:443
EXPOSE 3000:3000



# RUN echo "\n##############################\n1. Create a new user with adduser, 'su' into that user.\n2. 'yo meanjs' to scaffold your app in the current directory.\n3. Start mongo in the background (e.g. 'mongod &')\n##############################\n"
