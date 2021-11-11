FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/conf.d/proxy.template

CMD envsubst '${PROXY_PUBLIC_ADDRESS},${CORS_BACKEND}' < /etc/nginx/conf.d/proxy.template > /etc/nginx/conf.d/default.conf \
        && echo "### NGINX CONFIGURATION ####" \
        && cat /etc/nginx/conf.d/default.conf \
        && nginx -g 'daemon off;'