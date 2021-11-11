FROM node:latest as node
WORKDIR /app
COPY ./ /app/
RUN npm install
RUN npm run build -- --prod

FROM nginx:stable-alpine
COPY --from=node /app/dist/UTS /usr/share/nginx/html
COPY /nginx/nginx-custom.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx","-g","daemon off;"]
