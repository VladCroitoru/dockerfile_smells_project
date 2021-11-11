FROM nginx:mainline-alpine 
COPY mysite.template /etc/nginx/conf.d/mysite.template
CMD ["envsubst < /etc/nginx/conf.d/mysite.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]