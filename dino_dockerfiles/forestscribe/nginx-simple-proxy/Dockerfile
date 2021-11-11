from nginx:alpine
add nginx.vh.default.conf /etc/nginx/conf.d/default.conf.tpl
CMD /bin/sh -c "envsubst < /etc/nginx/conf.d/default.conf.tpl > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
