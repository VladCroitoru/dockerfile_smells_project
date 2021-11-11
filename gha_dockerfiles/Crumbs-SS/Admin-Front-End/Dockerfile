FROM node:12.2.0 as build
WORKDIR /app
COPY . /app
RUN npm install
RUN npm install -g @angular/cli@7.3.9
RUN npm run build
#CMD ng serve --host 0.0.0.0

FROM nginx:1.17.1-alpine
COPY --from=build /app/dist/CrumbsAdmin /usr/share/nginx/html
EXPOSE 80
#ENTRYPOINT ["nginx", "-g", "daemon off;"]