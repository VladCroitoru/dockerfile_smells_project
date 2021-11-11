FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN chown -R nginx:nginx /usr/share/nginx/html
RUN touch /var/run/nginx.pid 
RUN chown -R nginx:nginx /var/run/nginx.pid
RUN chown -R nginx:nginx /var/cache/nginx 
RUN chown -R nginx:nginx /var/log/nginx 
RUN chown -R nginx:nginx /etc/nginx/conf.d

COPY ./nginx.conf /etc/nginx/conf.d/
COPY dist/angular-starter/ /usr/share/nginx/html

USER nginx

EXPOSE 8080
