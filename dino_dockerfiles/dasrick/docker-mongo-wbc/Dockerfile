FROM ubuntu:14.04.2
MAINTAINER Alexander Miehe <alexander.miehe@gmail.com>
ENV MONGO_VERSION 3.0.6

RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \
    && apt-get update \
    && apt-get install -y mongodb-org=${MONGO_VERSION} mongodb-org-server=${MONGO_VERSION} mongodb-org-shell=${MONGO_VERSION} mongodb-org-mongos=${MONGO_VERSION} mongodb-org-tools=${MONGO_VERSION}

VOLUME /data/db

EXPOSE 27017 28017
CMD ["mongod", "-f", "/mongodb.conf"]
