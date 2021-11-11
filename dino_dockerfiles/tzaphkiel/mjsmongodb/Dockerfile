#
# MongoDB for MeteorJS applications
# Version: 3.0.4 (with updates blocked to that version)
# 
FROM ubuntu:14.04
MAINTAINER Sébastien Leroy <Leroy.milamber@gmail.com>

# Install MongoDB 
# @see http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/
# @see http://www.manuel-schoebel.com/blog/meteorjs-and-mongodb-replica-set-for-oplog-tailing
# 
# NB: running all commands in one line to avoid spanwning multiple containers
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \
  && echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list \
  && apt-get update \
  && apt-get install -y pwgen mongodb-org=3.0.8 mongodb-org-server=3.0.8 mongodb-org-shell=3.0.8 mongodb-org-mongos=3.0.8 mongodb-org-tools=3.0.8 \
  && echo "mongodb-org hold" | dpkg --set-selections \
  && echo "mongodb-org-server hold" | dpkg --set-selections \
  && echo "mongodb-org-shell hold" | dpkg --set-selections \
  && echo "mongodb-org-mongos hold" | dpkg --set-selections \
  && echo "mongodb-org-tools hold" | dpkg --set-selections

# where to store the data (host)
VOLUME /data/db

# Some configuration parameters
ENV MJSM_AUTH=true \
    MJSM_REPLICA_SET_NAME=meteormongo \
    MJSM_DATABASE_ENGINE=wiredTiger \
    MJSM_MONGO_PORT=27017 \
    MJSM_JOURNALING=true

# some init & config scripts
COPY assets/mongoInit.sh /mongoInit.sh
COPY assets/mongo.sh /mongo.sh
RUN chmod 755 /mongo.sh
RUN chmod 755 /mongoInit.sh

# since this actually fills-in the /data/db on the volume, it is not persisted 
# because no volume is associated from the host !!!
#RUN ["/bin/bash", "-c", "/mongoInit.sh"]

# expose the port host:container
EXPOSE ${MJSM_MONGO_PORT}

#ENTRYPOINT ["/mongo.sh"]

# Start the database
#CMD [""]
CMD ["/mongo.sh"]

