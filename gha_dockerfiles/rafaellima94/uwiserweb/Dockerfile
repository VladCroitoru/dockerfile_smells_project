FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install 
COPY . .

RUN npm run build

FROM nginx:stable-alpine as production-stage

ENV TZ=America/Sao_Paulo
COPY --from=build-stage /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
