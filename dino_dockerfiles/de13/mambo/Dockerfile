FROM centos:7
MAINTAINER de13 <stephane.beuret@data-essential.com>
RUN yum update -y && \
    yum install -y epel-release mod_wsgi && \
    yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm && \
    yum install -y pgadmin4 && \
    mkdir -p /var/log/pgadmin4 /var/lib/pgadmin4/{sessions,storage} && \
    touch /var/log/pgadmin4/pgadmin4.log && \
    chown -R apache. /var/log/pgadmin4 /var/lib/pgadmin4
COPY config_local.py /usr/lib/python2.7/site-packages/pgadmin4-web/
COPY pgadmin4.conf /etc/httpd/conf.d/
RUN /usr/bin/python /usr/lib/python2.7/site-packages/pgadmin4-web/setup.py && \
    chown apache. /var/lib/pgadmin4/pgadmin4.db
CMD /usr/sbin/apachectl -D FOREGROUND
