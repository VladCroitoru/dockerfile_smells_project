#Node Application
FROM centos:centos7

MAINTAINER fbgrecojr@me.com

RUN yum install -y epel-release \
	&& yum install -y nodejs npm

COPY ./package.json /src/package.json

RUN cd /src \
	&& npm install

COPY . /src

EXPOSE 8080

CMD ["node", "/src/app.js"]
