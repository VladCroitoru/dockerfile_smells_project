FROM endika/base
MAINTAINER me@endikaiglesias.com

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
    aptitude update && \
    aptitude install -y mongodb-org && \
    rm -rf /var/lib/apt/lists/*

VOLUME ["/data/db"]
WORKDIR /data
CMD ["mongod"]
# process
EXPOSE 27017
# http
EXPOSE 28017
