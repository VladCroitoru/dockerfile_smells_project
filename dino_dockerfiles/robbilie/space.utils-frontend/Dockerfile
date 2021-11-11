FROM node:alpine

# clone repo
RUN mkdir -p /usr/src/repo
WORKDIR /usr/src/repo

COPY package.json /usr/src/repo/

# Install Node.js dependencies
RUN yarn install --no-progress

COPY . .

# build
RUN NODE_ENV=production yarn run build -- --release

# create actual dir
RUN mv -f /usr/src/repo/build /usr/src/app
RUN rm -rf /usr/src/repo
WORKDIR /usr/src/app

# Install Node.js dependencies
RUN yarn install --production --no-progress && yarn cache clean

CMD [ "node", "server.js" ]
