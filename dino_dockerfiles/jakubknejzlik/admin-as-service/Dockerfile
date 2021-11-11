FROM node:alpine

COPY . /code

WORKDIR /code

RUN apk add --update git && rm -rf node_modules && npm install --unsafe-perm

ENTRYPOINT ["npm","start"]
