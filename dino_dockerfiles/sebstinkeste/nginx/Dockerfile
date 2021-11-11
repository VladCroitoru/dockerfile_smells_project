FROM nginx

MAINTAINER  Sébastien.Stinkeste (sebastien.stinkeste@alterway.fr)

COPY nginx.conf /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/sites-available/nginx.conf
#RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled

COPY entrypoint.sh /entrypoint.sh


EXPOSE 80 443


WORKDIR /var/www

CMD ["/entrypoint.sh"]

