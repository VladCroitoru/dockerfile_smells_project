FROM node:8.9.3-alpine
# Create app directory
RUN npm install -g babel-cli
RUN npm install -g pm2
RUN npm install -g babel-preset-env

RUN mkdir -p /usr/src/app 
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY  ./ .

RUN yarn install

# If you are building your code for production
#RUN npm install --only=production
RUN npm run build -- --release --docker
# Bundle app source
#, "--name 'webapp'", "-i max
CMD ["pm2", "start", "build/server.js", "--no-daemon"]
