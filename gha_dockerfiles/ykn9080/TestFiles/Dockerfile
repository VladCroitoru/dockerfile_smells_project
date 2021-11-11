FROM node:14-alpine AS builder
WORKDIR /app
COPY package.json ./

RUN npm install 
COPY . .
RUN npm run build

FROM nginx:1.19-alpine AS server
COPY --from=builder ./app/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
