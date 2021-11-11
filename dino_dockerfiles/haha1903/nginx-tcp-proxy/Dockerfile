FROM nginx
COPY nginx.conf.template /nginx.conf.template
EXPOSE 8888 80

CMD /bin/bash -c "envsubst < /nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"
