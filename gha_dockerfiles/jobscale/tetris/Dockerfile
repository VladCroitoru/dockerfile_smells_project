FROM nginx:alpine
WORKDIR /usr/share/nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
COPY public html
RUN chown -R nginx. html
