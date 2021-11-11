FROM node:16.9.1

ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV
ARG BUILD_HASH
ENV BUILD_HASH=$BUILD_HASH

# Install dependencies
WORKDIR /opt/app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Bundle app source
COPY . .
RUN yarn build

RUN chmod +x ./bin/wait-for-it.sh

CMD yarn start
