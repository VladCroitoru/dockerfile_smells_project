FROM node:4.2.1

ENV appdir=/usr/src/app

RUN mkdir -p ${appdir}
WORKDIR ${appdir}

RUN npm install express express-generator couchbase ottoman node-json-minify
RUN ${appdir}/node_modules/express-generator/bin/express -f ${appdir}
RUN npm install

ONBUILD COPY . ${appdir}

CMD ["npm", "start"]