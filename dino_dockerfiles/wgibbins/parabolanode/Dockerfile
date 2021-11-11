FROM    centos:centos6

# Enable EPEL for Node.js
RUN     rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# Install Node.js and npm
RUN     yum install -y npm

RUN cd /; mkdir src
# Bundle app source
COPY . /src
# Install app dependencies (or not - don't need any)
# RUN cd /src; npm install

EXPOSE  8080
CMD ["node", "/src/parabola.js"]