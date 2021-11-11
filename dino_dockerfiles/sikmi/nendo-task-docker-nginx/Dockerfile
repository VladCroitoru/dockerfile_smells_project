FROM nginx:1
#COPY config/nginx.conf /etc/nginx/nginx.conf
RUN rm -v /etc/nginx/conf.d/default.conf
COPY config/conf.d/nendo-task.conf /etc/nginx/conf.d/nendo-task.conf
