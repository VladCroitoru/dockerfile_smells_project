# Start with a node image with package info
# Installs *all* npm packages and runs build script
FROM node:14-alpine as builder
WORKDIR /app
COPY ["package*.json", "/app/"]
ENV NODE_ENV development
RUN npm ci
COPY [ ".", "/app/" ]
ENV NODE_ENV production
RUN npm run build

# Swaps to nginx and copies the compiled html ready to be serverd
# Uses a configurable nginx which can pass envionment variables to JavaScript
FROM nginx:1.19.7-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
