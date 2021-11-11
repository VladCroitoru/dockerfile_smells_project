FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY run.sh /etc/nginx/run.sh
COPY default.template /etc/nginx/conf.d/default.template

EXPOSE 80

CMD ["sh", "/etc/nginx/run.sh"]
