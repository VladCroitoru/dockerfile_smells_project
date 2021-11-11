FROM node:6.10.1-slim

RUN npm install -g gulp typescript@2.3.2 jasmine tslint

RUN cd /usr/local/lib/node_modules/npm && \
    npm install fs-extra && \
    sed -i -e s/graceful-fs/fs-extra/ lib/utils/rename.js && \
    sed -i -e s/fs\.rename/fs.move/ lib/utils/rename.js

COPY package.json tsconfig.json /app/be/service/
COPY src /app/be/service/src
WORKDIR /app/be/service

RUN npm install .
RUN tsc
CMD node dist/index.js
