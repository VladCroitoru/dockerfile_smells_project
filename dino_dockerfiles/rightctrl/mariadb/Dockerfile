FROM mariadb:10.1
MAINTAINER RightCtrl <support@rightctrl.com>
LABEL Vendor="RightCtrl"
LABEL License=GPLv2
LABEL Version=10.1

#COPY docker-entrypoint.sh /usr/local/bin/
#RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
EXPOSE 3306 4444 4567 4568
CMD ["mysqld"]