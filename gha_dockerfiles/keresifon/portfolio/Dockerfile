
FROM node:12-alpine AS builder
WORKDIR /web
COPY package*.json /web/
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.17
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /web/build /usr/share/nginx/html