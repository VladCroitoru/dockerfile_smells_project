
 # Centos OwnCloud latest

FROM centos:centos6
MAINTAINER Gabriel R F

#RUN yum -y update
RUN yum -y install https://anorien.csc.warwick.ac.uk/mirrors/epel/6/i386/epel-release-6-8.noarch.rpm && \
    yum -y install http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && \
    yum -y install nginx wget tar bzip2 unzip && \
    yum -y install php-fpm php-gd php-mysqlnd php-mbstring php-xml php-ldap --enablerepo=remi && \
    sed -i 's/user = apache/user = nginx/' /etc/php-fpm.d/www.conf && \
    sed -i 's/group = apache/group = nginx/' /etc/php-fpm.d/www.conf && \
    yum -y update --enablerepo=remi && \
    chown nginx:nginx /var/lib/php/session/ && \
    wget https://github.com/YOURLS/YOURLS/archive/master.zip && \
    unzip master.zip && \
    mv YOURLS-master /usr/share/nginx/yourls && \
    chown -R nginx:nginx /usr/share/nginx/yourls && \
    rm master.zip
     
ADD default.conf /etc/nginx/conf.d/default.conf
RUN service nginx start && service php-fpm start

ADD index.php /usr/share/nginx/yourls

ADD init.sh /init.sh
RUN chmod +x /init.sh

EXPOSE 80

CMD ["/init.sh"]
