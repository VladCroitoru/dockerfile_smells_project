FROM node:lts-alpine as build-stage
WORKDIR /app
ENV VUE_APP_API_URL='http://<STRAPI_URL>/graphql'

COPY package.json ./
RUN npm install
COPY . .
RUN npm run build


# étape de production
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]