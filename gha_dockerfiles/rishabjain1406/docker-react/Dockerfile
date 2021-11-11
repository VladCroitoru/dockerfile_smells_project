FROM node:alpine as builder
WORKDIR '/home/node/app'
COPY package.json .
RUN npm install
RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache
COPY . .
RUN npm run build

FROM nginx
EXPOSE 80
COPY --from=builder /home/node/app/build /usr/share/nginx/html


