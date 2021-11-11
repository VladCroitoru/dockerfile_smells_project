FROM node:8.0.0-alpine
LABEL maintainer "andrey@subbotin.me"

EXPOSE 3000
CMD ["yarn", "serve"]

ENV NODE_ENV production
ENV NPM_CONFIG_LOGLEVEL error
RUN npm install -g --non-interactive yarn@0.24.6

RUN mkdir -p /app
WORKDIR /app

ONBUILD COPY . /app/
ONBUILD RUN yarn install --ignore-scripts --prod --frozen-lockfile --no-emoji --non-interactive
