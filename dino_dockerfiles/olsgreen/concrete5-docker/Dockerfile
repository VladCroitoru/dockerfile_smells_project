FROM linode/lamp

MAINTAINER Oliver Green green2go@gmail.com

# Package source URL
ENV PACKAGE_URL http://www.concrete5.org/download_file/-/view/84191/

# If using <= 5.6.x set to true
ENV IS_LEGACY false

# MySQL & apache post-start stuff & first run
ADD run_stack /usr/local/bin/
ADD first_run /usr/local/bin/

# Set service configurations
RUN rm -v /etc/mysql/my.cnf
RUN rm -v /etc/apache2/apache2.conf
RUN rm -v /etc/apache2/sites-available/example.com.conf

ADD conf/my.cnf /etc/mysql/
ADD conf/apache2.conf /etc/apache2/
ADD conf/example.com.conf /etc/apache2/sites-available/

# Add our database setup script to the image 
# (replaces default DB & user with custom ones)
ADD database_setup /installer/

# Fix apache & PHP loose ends
RUN apt-get update
RUN apt-get install virt-what unzip wget php5-mysql php5-mcrypt php5-gd -y
RUN a2enmod rewrite

# Copy the apache base directory into the installer directory
RUN cp -R "/var/www/example.com" "/installer"

# Dowload, extract & place the concrete5 package
RUN  wget -O /installer/concrete.zip $PACKAGE_URL && \
  unzip /installer/concrete.zip -d /installer/ && \
  rm -Rf /installer/example.com/public_html/ && \
  mv /installer/concrete5*/ /installer/example.com/public_html/

# Move our .htaccess placeholder
ADD conf/htaccess.txt /installer/example.com/public_html/

# Startup
ENTRYPOINT ["/usr/local/bin/run_stack"]
