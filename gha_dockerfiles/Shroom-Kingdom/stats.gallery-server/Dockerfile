FROM node:14-bullseye-slim as build

COPY . .

RUN npm install
RUN npm run build

FROM node:14-bullseye-slim

WORKDIR /usr/src/app

RUN npm init -y
RUN npm install dotenv canvas pg

COPY --from=build dist .
COPY .env .
COPY fonts fonts

EXPOSE 3000
CMD [ "node", "-r", "dotenv/config", "." ]
