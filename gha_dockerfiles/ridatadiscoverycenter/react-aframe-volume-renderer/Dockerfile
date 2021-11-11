# build environment
FROM node:12-alpine as build
RUN apk add --no-cache git

WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build

# production environment
FROM nginx:1.16.0-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
