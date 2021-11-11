FROM node:16-alpine3.11 AS node

FROM node AS builder
WORKDIR /app

COPY package*.json ./
RUN npm install --silent

COPY . ./
RUN npm run compile

FROM node AS final
RUN mkdir -p /app/build

WORKDIR /app

RUN npm i -g pm2

COPY package*.json process.yml ./

RUN npm i --only=production  

COPY --from=builder /app/build ./build

EXPOSE 3001
ENTRYPOINT ["pm2-runtime", "./process.yml"]  