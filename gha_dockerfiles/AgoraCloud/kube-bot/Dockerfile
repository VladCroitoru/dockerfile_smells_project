# https://blog.logrocket.com/containerized-development-nestjs-docker/
FROM node:14.17-alpine as development
WORKDIR /agoracloud
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm i rimraf
RUN npm run build

FROM node:14.17-alpine as production
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
WORKDIR /agoracloud
COPY package*.json ./
RUN npm i
COPY . .
COPY --from=development /agoracloud/dist ./dist
CMD ["npm", "run", "start:prod"]