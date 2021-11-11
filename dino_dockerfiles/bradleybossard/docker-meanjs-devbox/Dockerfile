FROM bradleybossard/docker-node-devbox

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

RUN apt-get update

# Default directory mongo wants to put it's data
RUN mkdir -p /data/db

RUN apt-get install -y mongodb-org \
                       python

