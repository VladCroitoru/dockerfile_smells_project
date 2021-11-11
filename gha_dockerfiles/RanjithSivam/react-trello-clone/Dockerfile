FROM node:alpine
WORKDIR /app

COPY package*.json .
RUN apk add --no-cache --virtual .gyp \
        python2 \
        make \
        g++ \
    && npm i --legacy-peer-deps \
    && apk del .gyp

COPY . .
RUN echo "\nDISABLE_ESLINT_PLUGIN=true" >> .env

EXPOSE 3000
CMD ["npm", "start"]
