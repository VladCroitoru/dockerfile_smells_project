FROM node:6
#FROM centos:7
MAINTAINER Soichi Hayashi <hayashis@iu.edu>

#RUN yum -y install epel-release 
#RUN yum -y install npm node git

#RUN git clone https://github.com/soichih/gocdb2sls.git /gocdb2sls #1

COPY . /app
#WORKDIR /gocdb2sls/

#RUN npm install
RUN cd /app && npm install --production

RUN mkdir /cache
#it's user's responsibility to setup /gocdb2sls/config

CMD [ "/app/docker/start.sh" ]
