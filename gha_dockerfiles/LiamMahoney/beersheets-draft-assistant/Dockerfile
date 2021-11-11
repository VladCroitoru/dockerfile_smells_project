FROM node:current-alpine AS builder

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install --silent

COPY . ./

RUN npm run build

FROM node:current-alpine

WORKDIR /usr/share/app

COPY --from=builder /app/build ./build

RUN npm install -g serve

EXPOSE 5000

CMD [ "serve", "-s", "build" ]
