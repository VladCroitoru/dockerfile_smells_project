FROM stackbrew/debian:sid
RUN echo deb http://mirror.anl.gov/debian sid main > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y golang
RUN apt-get install -y npm
RUN apt-get install -y git
RUN apt-get install -y sudo
RUN ln -s /usr/bin/nodejs /usr/bin/node
