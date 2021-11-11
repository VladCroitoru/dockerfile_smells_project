# Angular build image
FROM node:latest as builder

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build


# Nginx image
FROM nginx:latest

COPY --from=builder /app/dist/bash-cmd-frontend /usr/share/nginx/html/

EXPOSE 80
