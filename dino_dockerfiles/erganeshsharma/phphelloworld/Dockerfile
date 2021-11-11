# Base Image
FROM ubuntu:16.04
# Update and Install php and apache2
RUN apt-get update -y && apt-get install -y php7.0 apache2 libapache2-mod-php7.0
RUN echo "ServerName "$(hostname -i) >> /etc/apache2/apache2.conf
RUN sed -i '/DirectoryIndex/c\        DirectoryIndex index.php index.html index.cgi index.pl index.php index.xhtml index.htm' /etc/apache2/mods-enabled/dir.conf
# Copy directory containing all php files onto the container
COPY ./src /var/www/html/
# Set working directory
WORKDIR /var/www/html
# Make port 80 available to the world outside this container 
EXPOSE 80
# To keep the apache server in foreground
CMD ["apachectl", "-D", "FOREGROUND"]
