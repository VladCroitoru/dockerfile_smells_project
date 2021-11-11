# pull official base image
FROM node:16.5.0-alpine
WORKDIR /usr/app
COPY package.json .
RUN npm install
RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache
COPY . .
CMD ["npm", "run", "start"]
