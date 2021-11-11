FROM bitnami/node:10 AS build
WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install --unsafe-perm

COPY . .
RUN npm run build


FROM bitnami/nginx:1.19 AS prod
WORKDIR /app

COPY --from=build /app/dist .
COPY ./nginx/alpinejs.conf /opt/bitnami/nginx/conf/server_blocks/nginx.conf