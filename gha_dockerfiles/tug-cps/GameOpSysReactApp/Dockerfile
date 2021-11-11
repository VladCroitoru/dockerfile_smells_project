FROM node:alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

COPY tsconfig.json .env.production ./
COPY ./public ./public
COPY ./src ./src

RUN npm run build:local

FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
