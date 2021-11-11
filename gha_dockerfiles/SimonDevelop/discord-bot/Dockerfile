FROM keymetrics/pm2:latest-alpine

# Bundle APP files
COPY commands /commands
COPY server.js .
COPY config.json .
COPY package.json .
COPY pm2.json .

# Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install

# Show current folder structure in logs
RUN ls -al -R

CMD ["pm2-runtime", "start", "pm2.json"]
