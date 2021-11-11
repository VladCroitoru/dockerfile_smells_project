#Dockerfile
FROM nginx:latest

COPY index.html /usr/share/nginx/html
COPY style.css /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80