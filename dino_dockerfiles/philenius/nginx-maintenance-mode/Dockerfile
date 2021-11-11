FROM nginx

COPY Dockerfile /Dockerfile

WORKDIR /var/www/

COPY css/ css/
COPY img/ img/
COPY index.html /var/www/

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8081
