FROM discourse/base:2.0.20171126

COPY ./site_settings.yml /var/www/discourse/config/
COPY ./admin.rake /var/www/discourse/lib/tasks/
COPY ./start-web.sh /var/www/discourse/

WORKDIR /var/www/discourse
CMD './start-web.sh'