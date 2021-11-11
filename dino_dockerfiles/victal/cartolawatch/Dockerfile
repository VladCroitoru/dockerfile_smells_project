FROM nginx:latest
COPY docker_files/application.template /etc/nginx/conf.d/application.template
COPY docker_files/startup.sh /usr/local/bin/startup.sh
COPY dist /usr/share/nginx/html/app

ENV NGINX_PORT 80
ENV API_ENDPOINT https://api.cartolafc.globo.com

CMD ["bash", "/usr/local/bin/startup.sh"]
