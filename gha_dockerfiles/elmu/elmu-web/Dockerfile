FROM node:16.10.0-alpine3.12

ENV NODE_ENV "production"

WORKDIR /app

COPY package.json yarn.lock /app/

RUN apk --no-cache add curl \
    && apk --no-cache --virtual build-dependencies add git \
    && yarn install --non-interactive --frozen-lockfile --check-files --production=true \
    && apk del build-dependencies

COPY . /app/

CMD ["node", "--experimental-json-modules", "--experimental-loader", "@educandu/node-jsx-loader", "--enable-source-maps", "src/index.js"]
