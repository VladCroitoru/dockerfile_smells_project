FROM centurylink/apache-php:latest
MAINTAINER CentruyLink

# Install packages
RUN apt-get update && \
 DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
 DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen unzip && \
 apt-get -y install mysql-client

# Download Concrete5 into /app
RUN rm -fr /app && mkdir /app && \
 curl -O http://www.concrete5.org/download_file/-/view/66159/8497 && \
 unzip 8497 -d /tmp  && \
 cp -a /tmp/concrete*/. ~/app

 rm -rf /tmp/concrete*

# Add script to create 'concrete5' DB
ADD run.sh run.sh
RUN chmod 755 /*.sh
RUN chmod -R 777 /var/www/html/config/ /var/www/html/files/ /var/www/html/packages/

EXPOSE 80
CMD ["/run.sh"]
