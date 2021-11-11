FROM nginx:1.13.0

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/conf.d/external/ && touch /etc/nginx/conf.d/external/users.htpasswd
COPY registry.conf /etc/nginx/conf.d/registry.conf

