FROM nginx

RUN apt-get update; apt-get upgrade -y

RUN  echo 'daemon off;' >> /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx"]
