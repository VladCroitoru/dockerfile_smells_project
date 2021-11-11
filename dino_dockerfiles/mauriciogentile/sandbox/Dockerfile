#node is a base image with nodejs and npm installed

FROM node

MAINTAINER @_mgentile

RUN npm install -g git+https://github.com/auth0/sandbox-worker.git

CMD ["sandbox-worker"]
