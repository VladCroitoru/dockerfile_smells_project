###########################################################
#
# Dockerfile for Varden
#
###########################################################

# Setting the base to php 5.6
FROM codenvy/php56_apache2
RUN sudo apt-get update
RUN sudo apt-get -y install php5-mysql git wget zip php5-curl libapache2-mod-php5
RUN sudo a2enmod php5
RUN sudo a2enmod rewrite
# ADD /src/index.php /var/www/html/
ADD dbdump/varden_dbdump.sql /docker-entrypoint-initdb.d
RUN sudo sed -i -e "s/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 15M/" /etc/php5/apache2/php.ini

# Maintainer
MAINTAINER Jørgen Johansen

#### Begin setup ####
# Change working directory
WORKDIR "/src"

# RUN sudo git clone https://github.com/jorjoh/Varden.git 
COPY ./ /var/www/html/
ADD dbconnection/dbcon.php /var/html/www/frontend/inc/functions
RUN sudo wget http://jorgenjohansen.no/vardenbilder/uploads.zip
# ADD uploads.zip /var/html/www/frontend/
RUN sudo unzip uploads.zip -d /var/www/html/frontend/

# Env variables
ENV SERVER_PORT 3000

# Expose 80
EXPOSE 80

