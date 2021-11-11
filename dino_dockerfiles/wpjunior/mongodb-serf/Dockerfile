# Dockerizing MongoDB: Dockerfile for building MongoDB images
# Based on ubuntu:latest, installs MongoDB following the instructions from:
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

FROM       mongo:3.4.1
MAINTAINER Wilson Júnior <wilsonpjunior@gmail.com>

RUN apt-get update && apt-get install -y unzip wget

# Create the MongoDB data directory
RUN mkdir -p /data/db

# install serf
RUN wget https://releases.hashicorp.com/serf/0.8.0/serf_0.8.0_linux_amd64.zip
RUN mv serf_0.8.0_linux_amd64.zip serf.zip
RUN unzip serf.zip
RUN mv serf /usr/bin/
RUN rm serf.zip

# entry points
ADD /initialize-serf.sh /usr/bin/initialize-serf.sh
ADD /initialize-ad.sh /usr/bin/initialize-ad.sh
ADD /initialize-shell.sh /usr/bin/initialize-shell.sh

ADD /mongodb-cluster-join.sh /usr/bin/mongodb-cluster-join.sh

ADD /run.sh /usr/bin/run.sh

RUN mkdir -p /etc/serf/scripts
ADD /event_handler.sh /etc/serf/scripts/event_handler.sh
ADD /mongodb_handler.sh /etc/serf/scripts/mongodb_handler.sh

# Expose port #27017 from the container to the host
EXPOSE 7946 7373
EXPOSE 27017
EXPOSE 27018
EXPOSE 27019
EXPOSE 28017

# Set /usr/bin/mongod as the dockerized entry-point application
ENTRYPOINT ["/usr/bin/run.sh"]
