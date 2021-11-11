FROM mhart/alpine-node:10.16.0

RUN mkdir -p /home/app
WORKDIR /home/app

# Downgrade to npm v5.6.0 because of this issue :
# https://github.com/npm/npm/issues/19989
# TODO: Use 'npm ci' when the issue gets fixed.
RUN npm --version
RUN npm install -g npm@5.6.0
RUN npm --version

RUN apk add --no-cache ffmpeg

ENV NODE_ENV production

COPY package*.json ./
RUN npm install

COPY . .
CMD ["npm", "start"]
