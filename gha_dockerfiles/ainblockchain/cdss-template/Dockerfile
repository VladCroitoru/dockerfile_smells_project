FROM node:14.17.5-alpine3.14

RUN mkdir /cdss
WORKDIR /cdss
ADD . /cdss
RUN yarn install
RUN yarn build

CMD [ "yarn", "start" ]
