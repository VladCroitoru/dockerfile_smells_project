FROM node:12-alpine as build
WORKDIR /usr/local/app
COPY ./ /usr/local/app/
RUN npm install
RUN npm run build

# Stage 2: Serve app with nginx server

FROM nginx:latest
COPY --from=build /usr/local/app/dist/personal-site /usr/share/nginx/html
EXPOSE 80
