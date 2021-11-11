FROM mhart/alpine-node:6.7.0

RUN apk add --no-cache git make gcc g++ python

RUN npm install -g bower

ADD package.json /src/package.json
ADD bower.json /src/bower.json
RUN cd /src; npm install && bower install --allow-root
ADD . /src/

WORKDIR /src

ENV NODE_ENV production

RUN npm run build

CMD npm run express
