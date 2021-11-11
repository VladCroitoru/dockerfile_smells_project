FROM nginx:1.17-alpine

COPY ./build /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./script/start.sh /usr/bin/start.sh

CMD ["/usr/bin/start.sh"]
