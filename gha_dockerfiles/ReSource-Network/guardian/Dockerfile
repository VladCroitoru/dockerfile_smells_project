FROM node:14.16.0-alpine

WORKDIR /app

RUN apk add git

COPY package.json yarn.lock ./prisma ./

RUN SKIP_POSTINSTALL=1 yarn install --production --pure-lockfile

COPY dist/ ./dist

EXPOSE 80

CMD [ "yarn", "start" ]
