FROM node:16-alpine

RUN apk update && apk add build-base git python3

COPY . .

RUN npm install -g npm
RUN npm install
RUN npm run build

EXPOSE 8081
ENV PORT 8081
ENV NODE_ENV production

CMD npm run start:prod
