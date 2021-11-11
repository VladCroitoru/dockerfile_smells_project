FROM	centos:centos7
MAINTAINER Chris Perry, cperry@resourcegovernance.org

# Enable EPEL for Node.js
RUN     rpm -Uvh https://rpm.nodesource.com/pub_4.x/el/7/x86_64/nodesource-release-el7-1.noarch.rpm

# Upgrade system
RUN     yum -y clean all
RUN     yum -y distro-sync
RUN     yum -y update
RUN     yum -y upgrade


# Install Node.js, npm, and git
RUN     yum install -y git nodejs npm

# Install dependancies
RUN		npm install -g bower forever

# Build src
ADD     package.json /tmp/package.json
RUN     cd /tmp && npm install --production
RUN     npm dedupe
RUN     mkdir -p /src && cp -a /tmp/node_modules /src
RUN		rm -R /tmp/node_modules
COPY	. /src
RUN		cd /src && bower install --allow-root

RUN     node -v
RUN     npm -v

EXPOSE  80

CMD     ["/src/node_modules/forever/bin/forever","/src/server.js"]