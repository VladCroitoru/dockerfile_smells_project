FROM node:13.12.0-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN mkdir -p /app/html
RUN cp -rf /app/build/* /app/html

# production environment
#FROM nginx:stable-alpine
#COPY --from=build /app/build /usr/share/nginx/html
#COPY client.nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000
#CMD ["nginx", "-g", "daemon off;"]

#CMD ["npm", "run", "start:prod"]
COPY ./entrypoint.client.sh ./
RUN chmod +x /app/entrypoint.client.sh
ENTRYPOINT ["sh", "/app/entrypoint.client.sh"]
