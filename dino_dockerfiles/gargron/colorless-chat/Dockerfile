FROM centos:centos6
MAINTAINER Eugen Rochko <eugen@zeonfederated.com>

ENV NODE_ENV production

RUN yum install -y epel-release
RUN yum install -y nodejs npm

COPY . /src
RUN cd /src; NODE_ENV=development npm install
RUN cd /src; /src/node_modules/.bin/webpack --progress --config ./webpack/webpack.config.prod.js
RUN cd /src; npm prune

EXPOSE 3000
CMD ["node", "/src/server/index.js"]
