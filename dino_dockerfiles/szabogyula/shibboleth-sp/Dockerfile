FROM httpd:2.4

# install required packages
RUN apt update
RUN apt install -y apache2 libapache2-mod-shib2

# configure shibboleth sp
ADD docker-config/shibboleth/shibboleth2.xml /etc/shibboleth/
ADD docker-config/shibboleth/attribute-map.xml /etc/shibboleth/
#ADD docker-config/shibboleth/shibd.logger /etc/shibboleth/
ADD docker-config/shibboleth/cert/* /etc/shibboleth/

#configure apache
ADD docker-config/apache_cert/*.key /etc/ssl/private/
ADD docker-config/apache_cert/*.pem /etc/ssl/certs/
ADD docker-config/apache_config/default-ssl.conf /etc/apache2/sites-available
RUN a2ensite default-ssl && a2dissite 000-default && a2enmod ssl && a2enmod rewrite

# install the runner
ADD docker-config/run.sh /run.sh

EXPOSE 443
CMD /run.sh
