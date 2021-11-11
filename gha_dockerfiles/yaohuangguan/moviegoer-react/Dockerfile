FROM hoosin/alpine-nginx-nodejs:latest AS build

WORKDIR /vite-app
COPY . .
RUN yarn install
RUN yarn build

#prepare nginx
FROM hoosin/alpine-nginx-nodejs:latest
COPY --from=build /vite-app/dist  /usr/share/nginx/html/
COPY --from=build /vite-app/package.json .

ARG NODE_ENV
RUN if [ $NODE_ENV = "development" ]; \
    then yarn install; \
    else rm /etc/nginx/conf.d/default.conf; \
    fi

COPY nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g","daemon off;"]