FROM node:alpine as build

WORKDIR /app

COPY package.json .
COPY yarn.lock .
RUN yarn install

COPY . .
RUN npm run build

FROM nginx:alpine

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/build /usr/share/nginx/html

