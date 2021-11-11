FROM node:14 AS buildClient

RUN mkdir -p app
WORKDIR /app

COPY ./client/package*.json ./
RUN npm install

COPY ./client .
RUN npm run build:prod

FROM node:14

RUN mkdir -p app
WORKDIR /app

COPY ./server/package*.json ./
RUN npm install

COPY ./server .
COPY --from=buildClient /app/dist /app/public

EXPOSE 3000

CMD ["npm", "start"]