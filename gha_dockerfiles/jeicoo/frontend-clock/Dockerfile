FROM node:14 AS builder

WORKDIR /opt/web
COPY package.json package-lock.json ./
RUN npm install

ENV PATH="./node_modules/.bin:$PATH"

COPY . ./
RUN ng build

FROM nginx:1.20-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /opt/web/dist/clock /usr/share/nginx/html
