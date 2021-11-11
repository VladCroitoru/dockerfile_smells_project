FROM node:lts-alpine
RUN apk add --no-cache git tzdata ; mkdir -p /usr/node_app

COPY . /usr/app
WORKDIR /usr/app

RUN npm install --production

CMD ["npm", "start"]
