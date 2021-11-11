FROM nginx:1.16.1-alpine
EXPOSE 8080
COPY default.conf /etc/nginx/conf.d/default.conf
COPY html/ /usr/share/nginx/html/
CMD ["nginx", "-g", "daemon off;"]
