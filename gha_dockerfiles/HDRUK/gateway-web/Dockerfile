FROM node:12 as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
COPY .env /app/.env
RUN npm install --silent
COPY . /app
RUN npm run build

# production environment
FROM nginx:latest
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/default.conf /etc/nginx/conf.d/
COPY nginx/error_pages /usr/share/nginx/html

EXPOSE 8080
CMD [ "nginx", "-g", "daemon off;"]
