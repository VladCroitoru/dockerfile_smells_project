FROM ubuntu:16.04

EXPOSE 80

COPY ./attach/setup_host.sh /docker-attach/
#RUN sudo chown root:root
#RUN dpkg-reconfigure dash
RUN ["/bin/bash", "/docker-attach/setup_host.sh"]
COPY ./attach/setup_phpmyadmin.sh /docker-attach/
#RUN ["/bin/bash", "/docker-attach/setup_phpmyadmin.sh"]
COPY ./attach/setup_joomla.sh /docker-attach/
RUN ["/bin/bash", "/docker-attach/setup_joomla.sh"]
COPY ./attach/fix_htaccess.sh /docker-attach/
RUN ["/bin/bash", "/docker-attach/fix_htaccess.sh"]

#RUN service --status-all
#CMD service apache2 start && service mysql start && tail -F /var/log/docker.log
COPY ./attach/wrapper.sh /docker-attach/
#CMD ["/bin/bash", "/docker-attach/wrapper.sh"]
