FROM library/debian:latest
MAINTAINER	riciba@gmail.com
RUN apt-get update && \
    apt-get -y install apache2 && \
    rm -rf /var/cache/apt /var/lib/dpkg && \
    sed 's/${APACHE_LOG_DIR}\/error.log/\/dev\/stderr/g' -i /etc/apache2/sites-available/000-default.conf && \
    sed 's/${APACHE_LOG_DIR}\/access.log/\/dev\/stdout/g' -i  /etc/apache2/sites-available/000-default.conf && \ 
    /bin/echo "hola mundo" > /var/www/html/index.html
EXPOSE 80
#CMD [ "8.8.8.8" ]

ENTRYPOINT [ "/usr/sbin/apachectl","-D", "FOREGROUND" ]

