FROM nodesource/vivid:LTS
MAINTAINER Prismatik Pty. Ltd. <david@prismatik.com.au>

RUN apt-get install -y git-core
COPY ./package.json /opt/app/

WORKDIR /opt/app

RUN npm install
RUN ln -s .. node_modules/root

ADD . /opt/app/

EXPOSE 3000

ENTRYPOINT ["node", "/opt/app/index.js"]
