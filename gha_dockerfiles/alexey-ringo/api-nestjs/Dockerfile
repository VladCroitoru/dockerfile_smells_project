FROM node:14.17-alpine as builder

ARG NODE_ENV=development
ENV NODE_ENV=${NODE_ENV}
ARG MAX_OLD_SPACE_SIZE=4096
ENV NODE_OPTIONS=--max-old-space-size=${MAX_OLD_SPACE_SIZE}

RUN apk --no-cache add python make g++ git

COPY package*.json ./
COPY yarn.lock ./
RUN yarn install

# The instructions for second stage
FROM node:14.17-alpine

# Installs latest Chromium (85) package.
RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      freetype-dev \
      harfbuzz \
      ca-certificates \
      ttf-freefont \
      nodejs \
      yarn

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

WORKDIR /usr/src/app
COPY --from=builder node_modules node_modules
COPY . .

RUN yarn build

CMD [ "yarn", "start:prod-server" ]
