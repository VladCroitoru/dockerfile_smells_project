FROM nginx:alpine

RUN apk --update add \
  && apk add --virtual curl

RUN mkdir -p /home/LogFiles \
 && mkdir -p /home/site/wwwroot

RUN rm -rf /usr/share/nginx/html \
 && rm -rf /var/log/nginx \
 && ln -s /home/site/wwwroot /usr/share/nginx/html \
 && ln -s /home/LogFiles /var/log/nginx

WORKDIR /home/site/wwwroot

RUN curl -SLO https://raw.githubusercontent.com/tkeydll/webapp_for_containers_volume_test/master/site.tar.gz
RUN tar zxvf site.tar.gz

#COPY site /usr/share/nginx/html
#COPY site /home/foo

# DON'T WORK
#COPY site/index.html /usr/share/nginx/html
#RUN chown nobody:nogroup /home/site/wwwroot/index.html
