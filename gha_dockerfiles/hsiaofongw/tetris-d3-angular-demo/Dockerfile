FROM node:14.17.4 as builder

WORKDIR /app

COPY [ "package.json", "package-lock.json", "./" ]

RUN npm ci

COPY . .

RUN npm run build

FROM nginx:latest

COPY --from=builder /app/dist/d3-demo /usr/share/nginx/html

COPY [ "default.conf", "/etc/nginx/conf.d/" ]

