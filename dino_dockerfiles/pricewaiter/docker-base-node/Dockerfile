FROM mhart/alpine-node:0.12.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY package.json /usr/src/app/
ONBUILD RUN npm install --no-optional && /bin/rm -rf /tmp/npm* /root/.npm /root/.node-gyp
ONBUILD COPY . /usr/src/app

CMD npm run start
