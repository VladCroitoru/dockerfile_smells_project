FROM ubuntu:xenial

RUN apt-get update && apt-get install -y apache2  curl && apt-get clean && \
    (curl -skL http://downloads.jboss.org/mod_cluster/1.3.1.Final/linux-x86_64/mod_cluster-1.3.1.Final-linux2-x64-so.tar.gz | tar xfz -) && \
    mv *.so /usr/lib/apache2/modules/ && \
    ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-enabled/ && \
    ln -s /etc/apache2/mods-available/proxy_ajp.load /etc/apache2/mods-enabled/ && \
    ln -s /etc/apache2/mods-available/proxy_cluster.load /etc/apache2/mods-enabled/ && \
    ln -s /etc/apache2/conf-available/cluster.conf /etc/apache2/conf-enabled/
    
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

ADD proxy_cluster.load /etc/apache2/mods-available/
ADD cluster.conf /etc/apache2/conf-available/



ADD html/ /var/www/html/

EXPOSE 80

ENTRYPOINT ["/usr/sbin/apache2ctl"]
CMD ["-D", "FOREGROUND"]
