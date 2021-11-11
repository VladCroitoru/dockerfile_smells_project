FROM node AS builder

WORKDIR /usr/src/app/

COPY package.json ./

RUN npm install

COPY ./ ./

RUN npm run build

FROM nginx

WORKDIR /usr/share/nginx/html/

COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /usr/src/app/build/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
