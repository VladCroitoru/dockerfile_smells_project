FROM jgsqware/express:4
MAINTAINER Julien Garcia Gonzalez <jgonzalez@wemanity.com>

WORKDIR /src

ADD package.json /src/package.json
RUN npm install

ADD . /src

ENTRYPOINT ["node","./bin/www"]
