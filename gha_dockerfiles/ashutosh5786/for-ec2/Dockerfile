FROM centos
RUN yum install nginx -y
RUN rm -rf /usr/share/nginx/html/*
COPY ./  /usr/share/nginx/html
CMD  ["nginx" "-s" "reload"]
EXPOSE 80
