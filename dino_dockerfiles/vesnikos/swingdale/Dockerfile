FROM nginx:alpine

COPY ./Viewer/ /usr/share/nginx/html
COPY ./nginx-conf/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]