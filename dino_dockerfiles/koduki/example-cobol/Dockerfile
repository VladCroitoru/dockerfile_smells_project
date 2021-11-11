FROM ubuntu

# install
RUN apt-get update -qq && apt-get install -y apache2 open-cobol

# apache settings
ADD resources/mime.conf /etc/apache2/mods-enabled/mime.conf
ADD resources/000-default.conf /etc/apache2/sites-enabled/000-default.conf
RUN a2enmod cgi
RUN /etc/init.d/apache2 restart 

# deploy cgi
RUN mkdir /app
WORKDIR /app

RUN mkdir bin && mkdir -p src/cobol
ADD src/cobol src/cobol
ADD src/cgi /var/www/html/ 
RUN chmod 705 /var/www/html/*.cgi

# run httpd
ADD resources/run-httpd.sh /usr/local/bin/run-httpd.sh
RUN chmod 705 /usr/local/bin/run-httpd.sh
CMD "/usr/local/bin/run-httpd.sh"
