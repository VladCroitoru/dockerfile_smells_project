# Inside frontend/Dockerfile
FROM node:16.10.0-slim as build

ADD . /code
WORKDIR /code
RUN npm ci
RUN npm run build

FROM nginx:1.21.3

ADD nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /code/build /usr/share/nginx/html
