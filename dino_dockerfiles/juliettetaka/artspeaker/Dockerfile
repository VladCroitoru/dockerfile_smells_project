# Set the base image to Ubuntu
FROM ubuntu:latest

# Update the repository
RUN apt-get update

# Download and Install
RUN apt-get install -y vim wget python-setuptools libpython2.7 python-flask nodejs-legacy python-pip npm
RUN pip install pymongo python-oauth2 flask-oauthlib

#Install last mongodb version to have text search feature
RUN cd /opt/ && \
    wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.6.tgz && \
    tar -zxvf mongodb-linux-x86_64-3.0.6.tgz && \
    mv mongodb-linux-x86_64-3.0.6 mongodb && \
    mkdir /opt/mongo-data

# Expose ports
EXPOSE 5000
EXPOSE 5001
EXPOSE 27017

ENV ARTSPEAKER_DEV=/opt/artspeaker_git
ENV PATH=${PATH}:/opt/mongodb/bin

COPY . ${ARTSPEAKER_DEV}
RUN cd ${ARTSPEAKER_DEV}/client/ && npm install && npm install -g grunt-cli

RUN mkdir /var/log/artspeaker

RUN chmod 777 ${ARTSPEAKER_DEV}/start.sh
ENTRYPOINT ["/opt/artspeaker_git/start.sh"]
