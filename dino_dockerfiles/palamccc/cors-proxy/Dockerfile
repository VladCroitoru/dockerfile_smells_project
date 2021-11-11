FROM node:6-alpine
WORKDIR /usr/src/app
EXPOSE 3000
ENV PORT 3000
ENV NODE_ENV production
COPY package.json yarn.lock ./
RUN yarn --production --pure-lockfile --ignore-optional --no-bin-links \
    && yarn cache clean \
    && rm -Rf /tmp/*
COPY src ./src
CMD [ "node", "--expose-gc", "src/index.js" ]