FROM ubuntu:latest

# Installing system dependencies
RUN apt-get update && \
    apt-get -y install curl

# Install MongoDB.
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list && \
    apt-get update && \
    apt-get install -y pwgen mongodb-org mongodb-org-server mongodb-org-shell mongodb-org-mongos mongodb-org-tools && \
    echo "mongodb-org hold" | dpkg --set-selections && \
    echo "mongodb-org-server hold" | dpkg --set-selections && \
    echo "mongodb-org-shell hold" | dpkg --set-selections && \
    echo "mongodb-org-mongos hold" | dpkg --set-selections && \
    echo "mongodb-org-tools hold" | dpkg --set-selections

COPY pushbullet.sh /pushbullet.sh
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /*.sh

# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory.
WORKDIR /data

# Expose port
EXPOSE 27017

ENTRYPOINT ["/entrypoint.sh"]

# Define default command.
CMD ["mongod"]
