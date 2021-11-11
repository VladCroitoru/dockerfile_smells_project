FROM node:14.17.6-alpine3.11 AS build
WORKDIR /app
COPY package.json package.json
RUN yarn install
COPY . .
RUN yarn build

FROM nginx:1.19-alpine
COPY --from=build /app/build /app/site
COPY nginx.conf /etc/nginx/nginx.conf