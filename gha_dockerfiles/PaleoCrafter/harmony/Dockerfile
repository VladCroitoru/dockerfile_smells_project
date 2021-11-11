FROM node:16-alpine AS base_node_modules

WORKDIR /app
COPY ./package.json ./package-lock.json /app/
RUN npm install --omit dev

FROM base_node_modules AS build

RUN npm install
COPY . /app
RUN npm run build

FROM node:16-alpine

WORKDIR /app

COPY --from=base_node_modules /app/node_modules /app/node_modules
COPY --from=build /app/dist /app/dist

CMD ["node", "dist/bot.js"]
