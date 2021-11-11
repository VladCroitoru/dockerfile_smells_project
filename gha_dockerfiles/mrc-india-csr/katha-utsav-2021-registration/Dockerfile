FROM node:14.15.4-stretch-slim as build
WORKDIR /home/app
COPY package*.json ./
RUN npm install --only=production
RUN npm ci --only=production
COPY . .
EXPOSE 3002
CMD npm run dev