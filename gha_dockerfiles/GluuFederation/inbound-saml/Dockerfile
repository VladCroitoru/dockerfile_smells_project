# syntax=docker/dockerfile:1

FROM node:alpine
ENV NODE_ENV=prod
WORKDIR /code
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5000
CMD [ "npm", "run", "start"]
