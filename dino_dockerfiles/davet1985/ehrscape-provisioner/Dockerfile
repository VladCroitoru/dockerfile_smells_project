FROM centos:centos6

# Enable EPEL for Node.js
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum install -y git
RUN yum install -y npm

ADD package.json /src/package.json
RUN cd /src; npm install

RUN npm install -g bower gulp nodemon

COPY . /src

RUN cd /src; bower install --allow-root
RUN cd /src; gulp

EXPOSE 8080
CMD ["node", "/src/bin/www"]
