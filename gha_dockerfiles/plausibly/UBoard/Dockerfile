# => Build client
FROM node:16-alpine as client_builder
WORKDIR /app/client
COPY client .
RUN yarn install --production && yarn run build

# => Build server
FROM node:16-alpine as server_builder
WORKDIR /app/server
COPY server .
RUN yarn install && yarn run build

# => Run container
FROM nginx:1.20-alpine as base

# Default port exposure
EXPOSE 80

# Add nodejs
RUN apk add --update nodejs
RUN apk add --update sqlite

# Nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

# Static build
WORKDIR /app
COPY --from=client_builder /app/client/build/. /usr/share/nginx/html/.
COPY --from=server_builder /app/server server

# Start Nginx server
CMD /bin/sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx && node server/build/server.js