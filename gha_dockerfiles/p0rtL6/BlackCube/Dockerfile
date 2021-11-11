FROM node:16.8-alpine

ARG BOT_TOKEN
ENV token $BOT_TOKEN

ARG CLIENT_ID
ENV clientId $CLIENT_ID

ARG MONGODB_URI
ENV mongoIp $MONGODB_URI

ENV NODE_ENV production

ADD package.json /tmp/package.json

# Remove the old build directory
RUN rm -rf build

# Install the dependancies
RUN cd /tmp && npm install -q

ADD ./ /src

# Copy to dependancies to the src directory
RUN rm -rf /src/node_modules && cp -a /tmp/node_modules /src/

WORKDIR /src

# Run the built application
CMD npx pm2-runtime start ./src/APFPHelper.js
