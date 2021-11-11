FROM centos:centos7

MAINTAINER modonnel@tudor.com

#enable EPEL for Node.js
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

# Install Node...
RUN yum install -y npm

#Copy app to /src
COPY . /src

# Install app and dependencies into /src
RUN cd /src; npm install

EXPOSE 8080

CMD cd /src && node ./app.js