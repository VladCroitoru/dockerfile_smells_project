FROM node:10.19.0-alpine
WORKDIR /usr/src/app
COPY package*.json ./
EXPOSE 8080
ENV NODE_ENV production
RUN npm install
COPY . .
CMD [ "npm", "start" ]
