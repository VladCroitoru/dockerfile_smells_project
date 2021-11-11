FROM quay.io/kushalsamota/centos:latest
RUN  yum install httpd -y
RUN  echo "<h1> Hello Everyone 12345678 </h1>" > /var/www/html/index.html
CMD  ["/usr/sbin/httpd","-D","FOREGROUND"]
