FROM centos:centos6

MAINTAINER nigelpoulton@hotmail.com

# enable EPEL for Node.js
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

# install node
RUN yum install -y npm

# copy app to src
COPY . /src

# install app and dependencies into /src
RUN cd /src; npm install

EXPOSE 8080

CMD cd /src && node ./app.js