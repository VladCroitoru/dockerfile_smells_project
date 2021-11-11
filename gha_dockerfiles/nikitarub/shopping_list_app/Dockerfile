FROM node:16
WORKDIR /app/app
ADD ./app/package.json ./app/yarn.lock /app/app/
RUN yarn
ADD . /app
ENTRYPOINT [ "yarn", "start" ]
