FROM alpine:latest
LABEL maintainer="gwaewion@gmail.com"
EXPOSE 80
COPY run.sh /root/
COPY pfadmin.conf /root/
COPY config.inc.php /root/

ENV DB_SERVER_ADDRESS CHANGE_ME
ENV DB_NAME CHANGE_ME
ENV DB_USER CHANGE_ME
ENV DB_USER_PASSWORD CHANGE_ME
ENV SMTP_SERVER_ADDRESS CHANGE_ME
ENV MAIL_FQDN CHANGE_ME

RUN apk update
RUN apk add nginx php7 php7-mysqli php7-fpm php7-session php7-mbstring php7-imap git
RUN cp /root/pfadmin.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /var/www/*
RUN git clone https://github.com/postfixadmin/postfixadmin.git /var/www/
RUN cp /root/config.inc.php /var/www/
RUN sed -i "s/\$CONF\['database_host'\] = '';/\$CONF\['database_host'\] = '"${DB_SERVER_ADDRESS}"';/" /var/www/config.inc.php
RUN sed -i "s/\$CONF\['database_user'\] = '';/\$CONF\['database_user'\] = '"${DB_USER}"';/" /var/www/config.inc.php
RUN sed -i "s/\$CONF\['database_password'\] = '';/\$CONF\['database_password'\] = '"${DB_USER_PASSWORD}"';/" /var/www/config.inc.php
RUN sed -i "s/\$CONF\['database_name'\] = '';/\$CONF\['database_name'\] = '"${DB_NAME}"';/" /var/www/config.inc.php
RUN sed -i "s/\$CONF\['smtp_server'\] = '';/\$CONF\['smtp_server'\] = '"${SMTP_SERVER_ADDRESS}"';/" /var/www/config.inc.php
RUN sed -i "s/\$CONF\['admin_email'\] = '';/\$CONF\['admin_email'\] = '"${MAIL_FQDN}"';/" /var/www/config.inc.php
RUN sed -i "s/change-this-to-your.domain.tld/"${MAIL_FQDN}"/g" /var/www/config.inc.php
RUN sed -i "s/user nginx;/daemon off;\n\nuser nginx;/" /etc/nginx/nginx.conf
RUN mkdir /var/www/templates_c
RUN chmod 777 /var/www/templates_c
RUN chown -R nginx:nginx /var/www 
RUN mkdir /run/nginx 
RUN chown nginx:nginx /run/nginx

CMD ["sh", "/root/run.sh"]
