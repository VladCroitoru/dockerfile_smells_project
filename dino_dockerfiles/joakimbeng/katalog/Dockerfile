FROM mhart/alpine-node:6

# Add dumb-init (see: https://nodesource.com/blog/8-protips-to-start-killing-it-when-dockerizing-node-js/)
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

ENV PORT 5005

EXPOSE 5005

WORKDIR /app

ADD package.json /app/package.json

RUN npm install --production && npm cache clean

ADD . /app

CMD ["dumb-init", "npm", "start", "--silent"]
