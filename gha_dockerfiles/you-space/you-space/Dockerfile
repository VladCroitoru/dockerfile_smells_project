### First stage ###
FROM node:14-alpine AS build

WORKDIR /app

COPY . .

RUN npm install

RUN yarn --cwd dashboard

RUN npm run build --prefix dashboard

RUN npm run build

##########################

### Second stage ###
FROM node:14-alpine

COPY --from=build /app/build /app

RUN apk add git

WORKDIR /app

RUN npm ci --production

CMD ["node", "ace", "start"]