# base image
FROM node:9

# copy the app
WORKDIR /usr/src/app
COPY . /usr/src/app/

# build the client app
WORKDIR /usr/src/app/client-web
RUN yarn install
RUN yarn build
RUN rm -r /usr/src/app/client-web/node_modules

# prepare the server
WORKDIR /usr/src/app/server
RUN yarn install --production

# configure the runtime
CMD [ "/usr/local/bin/node", "/usr/src/app/server/src/index.js" ]
EXPOSE 3001
