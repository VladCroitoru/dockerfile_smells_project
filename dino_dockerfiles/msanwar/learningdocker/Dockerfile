From centos
run yum -y install httpd
env APACH_LOG_DIR /var/log/httpd
copy index.html /var/www/html
entrypoint ["/usr/sbin/httpd","-D","FOREGROUND"]
