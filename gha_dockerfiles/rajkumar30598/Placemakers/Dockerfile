FROM nginx:alpine

COPY ./dist/placemakers /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf

RUN nginx -t

EXPOSE 80