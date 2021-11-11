FROM node:lts-alpine as builder
COPY . /app
WORKDIR /app
RUN npm install
RUN npm run build

FROM nginx:alpine
COPY docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx/docker-entrypoint.sh /docker-entrypoint.sh
COPY --from=builder /app/build/. /usr/share/nginx/html/
RUN chmod +x /docker-entrypoint.sh
EXPOSE $PORT
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
