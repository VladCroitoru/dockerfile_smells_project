FROM ubuntu:trusty
MAINTAINER David Yang <david.g.yang@gmail.com>

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
# RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

# RUN rm -rf /var/lib/apt/lists/partial/*
RUN apt-get update
#RUN apt-get install -y mongodb-org
RUN apt-get install -y mongodb git python build-essential curl libssl-dev
RUN apt-get install --yes --force-yes libgtk2.0-0 libidn11 libglu1-mesa
# RUN service mongodb start

RUN mkdir -p /data/db

# install Postgres http://tecadmin.net/install-postgresql-server-on-ubuntu/
#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
#RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
#RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib
# RUN service postgresql start



RUN mkdir /Development

RUN cd /Development && git clone --branch v8.1.4 git://github.com/nodejs/node
RUN cd /Development/node && ./configure && make && make install
RUN rm -rf /Development/node

RUN chmod 777 -R /Development

RUN npm install -g bower express mongoose phantomjs-prebuilt
# RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

EXPOSE 80:80
EXPOSE 443:443
EXPOSE 3000:3000

RUN echo "\n##############################\n1. Create a new user with adduser, 'su' into that user.\n2. 'yo meanjs' to scaffold your app in the current directory.\n3. Start mongo in the background (e.g. 'mongod &')\n##############################\n"
