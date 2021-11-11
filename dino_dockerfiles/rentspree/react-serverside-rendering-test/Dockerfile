FROM node:8.9.4-alpine

# RUN yarn global add node-gyp

# Create app directory
RUN mkdir -p /app
WORKDIR /app


ADD package.json /app/package.json
RUN yarn install --silent --prod

ADD configs /app/configs
ADD libs /app/libs
ADD index.js /app/index.js

CMD ["yarn", "run", "start"]

