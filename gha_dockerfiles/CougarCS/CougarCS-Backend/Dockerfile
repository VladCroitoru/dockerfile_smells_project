FROM node:erbium-alpine3.11 AS build

ENV NODE_ENV prod

WORKDIR /app

COPY package.json .babelrc ./

RUN npm install

COPY ./src ./src

RUN npm run build

RUN npm prune --production


FROM node:erbium-alpine3.11




WORKDIR /app

RUN chown -R 1000:1000 /app

RUN chmod 755 /app

USER 1000

COPY --from=build /app/node_modules ./node_modules

COPY --from=build /app/dist ./dist

EXPOSE 4000

CMD ["node", "./dist/server.js"]
