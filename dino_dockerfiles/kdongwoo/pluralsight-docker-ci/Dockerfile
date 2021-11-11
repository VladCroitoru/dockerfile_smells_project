FROM centos:centos6
MAINTAINER kdongwoo@gmail.com

RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# Install Node...
RUN yum install -y npm

# Copy app to /src
COPY . /src

COPY . /src

RUN cd /src; npm install

EXPOSE 8888
CMD cd /src && node ./app.js
