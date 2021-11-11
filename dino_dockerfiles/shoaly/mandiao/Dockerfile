FROM nginx:1.11



# ADD  default.conf /etc/nginx/conf.d/default.conf
ADD  default.tpl /etc/nginx/conf.d/default.tpl
#CMD /bin/bash -c "envsubst '\$TARGET_DOMAIN' < /etc/nginx/conf.d/default.tpl > /etc/nginx/conf.d/default.conf "
#CMD [ "nginx" , "-g", "daemon off;"]
#ADD  sites-enabled/*    /etc/nginx/conf.d/