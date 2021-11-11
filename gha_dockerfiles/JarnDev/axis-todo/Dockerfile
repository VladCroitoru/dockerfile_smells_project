FROM node:14.15.4 AS builder

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

FROM node:14.15.4

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/tracing.js ./ 
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/src/database/docker-config.json ./config/config.json
COPY --from=builder /app/src/database/migrations ./migrations
COPY --from=builder /app/src/database/seeders ./seeders
CMD ["npm", "run", "start:prod"]