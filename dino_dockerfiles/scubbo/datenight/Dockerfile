FROM ubuntu:14.04

# Install dependencies
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN apt-get update
RUN apt-get install -y git curl apache2 php5 libapache2-mod-php5 php5-mcrypt php5-mysql python3.4 python3-pip
RUN pip3 install passlib
RUN pip3 install boto3

# Install app
RUN rm -rf /var/www/*
RUN mkdir /var/www/datenight
ADD src /var/www/datenight
RUN rm /etc/apache2/sites-enabled/*
RUN rm /etc/apache2/sites-available/*
ADD conf/apache.conf /etc/apache2/sites-available/datenight.conf
RUN ln -s /etc/apache2/sites-available/datenight.conf /etc/apache2/sites-enabled/datenight.conf

# Configure apache
RUN a2enmod rewrite
RUN a2enmod php5
RUN a2enmod cgi
RUN a2ensite datenight
RUN chown -R www-data:www-data /var/www
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

ENTRYPOINT ["apachectl", "-DFOREGROUND"]
