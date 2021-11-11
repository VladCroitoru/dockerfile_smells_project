# build stage
FROM node:14-alpine as build
WORKDIR /app

COPY package.json ./
RUN npm i --silent

COPY . ./
RUN npm run build

# deployement stage
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
