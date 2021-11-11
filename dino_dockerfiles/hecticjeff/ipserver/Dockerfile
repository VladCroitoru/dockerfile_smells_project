# DOCKER-VERSION 0.7.1
FROM centos:6.4

# Enable EPEL for Node.js
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# Install Node.js and npm
RUN yum install -y npm

# Bundle app source
ADD . /app

# Install app dependencies
RUN cd /app; npm install

ENV NODE_ENV production
ENV PORT 80

EXPOSE 80

CMD ["node", "/app/server.js"]
