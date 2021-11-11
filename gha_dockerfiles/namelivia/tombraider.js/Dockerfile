# base builder stage
FROM node:12-stretch as base-builder
WORKDIR /app
COPY package*.json ./
COPY . .

# build stage for testing
FROM base-builder as testing
RUN npm install --also=dev
