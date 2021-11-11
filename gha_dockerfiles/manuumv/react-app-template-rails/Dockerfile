# Builder
FROM node:alpine AS builder
COPY / ./app
WORKDIR /app

RUN npm install && npm run build:prod

# Build
FROM node:alpine
COPY --from=builder /app/dist ./app/dist

WORKDIR /app
COPY server/index.js ./
COPY server/package.json ./

# Dependencies
ENV NODE_ENV=production PUBLIC_PATH="./dist"
RUN npm install

# Port exposing
EXPOSE 8000

CMD ["npm", "start"]
