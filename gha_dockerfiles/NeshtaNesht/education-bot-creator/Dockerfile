FROM node:12-alpine as build
WORKDIR /app
COPY ./package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.16.0-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80 443
ADD nginx/nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]