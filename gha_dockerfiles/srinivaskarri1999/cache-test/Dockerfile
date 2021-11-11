FROM node:alpine
WORKDIR /opt
COPY package*.json /opt
RUN npm ci
COPY . .
RUN npm run build
