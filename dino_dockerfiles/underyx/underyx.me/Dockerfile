FROM node:15-slim as gatsby

WORKDIR /app

COPY package.json package-lock.json ./
RUN apt-get update &&\
  apt-get install libgl1-mesa-glx libvips libfribidi0 libharfbuzz-dev -y --no-install-recommends &&\
  npm ci --legacy-peer-deps

COPY . ./
RUN npx gatsby build

FROM nginx:1.17-alpine

COPY --from=gatsby /app/public /usr/share/nginx/html
COPY static/* /usr/share/nginx/html/
COPY nginx.vhost.conf /etc/nginx/conf.d/default.conf
