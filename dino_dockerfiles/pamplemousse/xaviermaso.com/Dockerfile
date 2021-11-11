FROM node:14

RUN apt-get update && apt-get install apt-transport-https

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD ARG NODE_ENV
ONBUILD ENV NODE_ENV $NODE_ENV

COPY package.json /usr/src/app/
COPY yarn.lock /usr/src/app/

RUN yarn install --production

COPY back /usr/src/app/back
COPY dist /usr/src/app/dist

EXPOSE 8000

USER node

CMD ["npm", "run", "start:back"]
