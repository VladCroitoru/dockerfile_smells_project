FROM node:14-alpine AS builder

WORKDIR /app
COPY . .
RUN npm i && npm run build

FROM nginx:alpine

WORKDIR /usr/share/nginx/html
COPY --from=builder /app/build .
