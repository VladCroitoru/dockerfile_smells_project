# use a moving tag for now
FROM node:16

ENV APP_UID=9999
ENV APP_GID=9999

RUN groupmod -g $APP_GID node
RUN usermod -u $APP_UID -g $APP_GID node

RUN mkdir -p /usr/src
RUN chown -R node /usr/src
USER node
WORKDIR /usr/src

COPY . /usr/src

RUN npm ci
RUN npm run build

EXPOSE 3000
CMD ["node", "/usr/src/node_modules/.bin/next", "start"]
