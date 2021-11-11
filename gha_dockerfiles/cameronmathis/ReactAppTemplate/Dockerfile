FROM node:10-alpine AS build
ENV NODE_ENV production
WORKDIR /app
COPY . /app
RUN npm ci --only=production
CMD "npm" "start"
