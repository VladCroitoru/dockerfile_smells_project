
FROM nginx:1.15-alpine
WORKDIR /usr/src/app
COPY . .
COPY ./ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
