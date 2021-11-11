FROM node:6.6.0

ENV WORK_DIR /root

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
#RUN npm install -g npm
RUN apt-get update -y
RUN apt-get install -y mongodb-org

VOLUME ${WORK_DIR}
