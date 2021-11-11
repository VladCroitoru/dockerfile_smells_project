FROM node:8.9.3-alpine
# Create app directory
RUN npm install -g babel-cli
RUN npm install -g babel-preset-env

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY  ./ .

RUN yarn install
# If you are building your code for production
# RUN npm install --only=production
RUN yarn run build -- --release --docker
# Bundle app source
CMD ["node_modules/pm2/bin/pm2", "start", "build/server.js, "--name 'webapp'", "-i max"]

