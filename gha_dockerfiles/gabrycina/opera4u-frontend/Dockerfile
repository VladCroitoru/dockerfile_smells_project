FROM node:14.1-alpine as build

WORKDIR /app

COPY . /app

ENV PATH /app/node_modules/.bin:$PATH

RUN yarn config delete proxy
RUN npm config rm proxy

RUN npm config rm https-proxy

RUN npm install

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY proxy/nginx.conf /etc/nginx/conf.d

EXPOSE 80
# start nginx 
CMD ["nginx", "-g", "daemon off;"]