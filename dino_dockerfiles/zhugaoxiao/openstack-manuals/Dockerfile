FROM centos

MAINTAINER zhugaoxiao <zhugaoxiao@gmail.com>

RUN yum install -y epel-release gcc python-devel libxml2-devel libxslt-devel git httpd

RUN yum install -y python-pip; \
    yum clean all
    
RUN pip install tox

RUN mkdir /home/git; \
    cd /home/git; \
    git clone https://github.com/openstack/openstack-manuals.git; \
    cd openstack-manuals; \
    tox -e checkbuild; \
    rm -rf /var/www/html; \
    rm -f /etc/httpd/conf.d/welcome.conf; \
    mv doc /var/www/html

EXPOSE 80

ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
