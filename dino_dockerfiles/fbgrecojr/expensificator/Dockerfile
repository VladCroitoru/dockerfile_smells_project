#Node Application
FROM centos:centos7

MAINTAINER fbgrecojr@me.com

RUN yum install -y epel-release \
	&& yum install -y nodejs npm

ADD . /src
WORKDIR /src

RUN cd /src \
	&& npm install \
        && npm install --global gulp-cli \
	&& npm install gulp --save-dev

EXPOSE 8080

CMD ["gulp"]