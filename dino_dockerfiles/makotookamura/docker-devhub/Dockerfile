FROM ubuntu:14.04
MAINTAINER makoto_okamura

RUN rm /sbin/initctl && \
  ln -s /bin/true /sbin/initctl && \
  dpkg-divert --local --rename --add /etc/init.d/mongod && \
  ln -s /bin/true /etc/init.d/mongod

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \
  echo 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse' > /etc/apt/sources.list.d/mongodb.list

RUN apt-get update && \
  apt-get -y install git nodejs npm wget \
  mongodb-org=3.2.11 mongodb-org-server=3.2.11 \
  mongodb-org-shell=3.2.11 mongodb-org-mongos=3.2.11 \ 
  mongodb-org-tools=3.2.11 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN npm -g -y install npm@3.8.2 n && n 4.4.0
RUN git clone https://github.com/volpe28v/DevHub DevHub
WORKDIR DevHub
RUN npm install

COPY ./Devhub/views/index.ejs /Devhub/views/index.ejs
COPY start.sh /usr/local/bin
RUN chmod 755 /usr/local/bin/start.sh

EXPOSE 3000

ENTRYPOINT ["/usr/local/bin/start.sh"]
