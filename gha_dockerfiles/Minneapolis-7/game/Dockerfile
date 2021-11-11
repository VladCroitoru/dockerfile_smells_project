FROM node:14-alpine AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM node:14-alpine
COPY --from=build /app/dist /dist

COPY --from=build /app/node_modules /node_modules
COPY --from=build /app/package.json /package.json

COPY --from=build /app/start-server.js /start-server.js

COPY --from=build /app/db /db
COPY --from=build /app/.sequelizerc /.sequelizerc
COPY --from=build /app/src/shared/lang /src/shared/lang

CMD POSTGRES_DB_HOST=postgres npm run serve:prod
