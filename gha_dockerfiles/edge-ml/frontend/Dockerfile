# build environment
FROM node:latest as build-step
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@1.1.1 -g --silent
COPY . ./
RUN npm run build

FROM nginx
COPY --from=build-step /usr/src/app/build /usr/src/app/build
