FROM node:alpine
MAINTAINER Alan Gutierrez <alan@prettyrobots.com>

WORKDIR /app

COPY package*.json .
RUN npm install --no-package-lock --no-save --only=production

COPY ./ ./
