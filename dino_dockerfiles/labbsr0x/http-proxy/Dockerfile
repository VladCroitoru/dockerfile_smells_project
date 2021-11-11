FROM nginx:1.9

COPY nginx.template /tmp/nginx.template

CMD /bin/bash -c "envsubst \"`printf '${%s} ' $(bash -c "compgen -A variable")`\" < /tmp/nginx.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"