FROM node:14.18.0-alpine3.14 as dev
RUN npm i -g typescript
WORKDIR /app
COPY ./package*.json ./
RUN npm i
COPY . .
RUN tsc

FROM node:14.18.0-alpine3.14 as prod
COPY --from=dev /app /app
WORKDIR /app
CMD ["node", "/app/www/index.js"]