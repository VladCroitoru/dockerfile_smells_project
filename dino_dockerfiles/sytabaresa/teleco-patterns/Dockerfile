FROM node:alpine as builder

COPY . /home/node/app

WORKDIR /home/node/app

RUN npm install && npm run build

FROM nginx:alpine

COPY --from=builder /home/node/app/dist/ /usr/share/nginx/html
