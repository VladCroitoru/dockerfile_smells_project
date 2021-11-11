FROM node:14

ADD .yarn /build/.yarn
ADD .yarnrc.yml /build
ADD yarn.lock /build
ADD package.json /build
WORKDIR /build
RUN yarn install

ADD . /build
RUN yarn build
ENTRYPOINT yarn start

