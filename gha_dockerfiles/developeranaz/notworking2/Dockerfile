FROM developeranaz/aria2-webui
RUN apt update -y
RUN apt install nginx -y
COPY aria2x /usr/bin/aria2x
COPY default /default
COPY apache2x /usr/bin/apache2x
RUN chmod +x /usr/bin/aria2x
RUN chmod +x /usr/bin/apache2x
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY index.html /index.html
RUN cat /index.html >/var/www/html/index.html
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh
