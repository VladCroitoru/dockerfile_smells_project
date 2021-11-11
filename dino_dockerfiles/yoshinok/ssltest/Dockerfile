FROM nginx:latest
COPY www.kohzee.xyz.crt /etc/nginx
COPY www.kohzee.xyz.pem /etc/nginx
COPY default.conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]

