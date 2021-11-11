FROM node:12-slim AS build
RUN apt update
RUN apt install git -y
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:12-slim
RUN apt update
RUN apt install git -y
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm ci
RUN npm cache clean --force
COPY --from=build /usr/src/app/bin bin

ENV NODE_ENV="production"
RUN npm install -g localtunnel
CMD [ "npm", "start" ]
