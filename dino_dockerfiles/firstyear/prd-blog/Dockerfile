
FROM centos:7
MAINTAINER wibrown@redhat.com

EXPOSE 8080

# Install apache
# Install tinkerer, this is from pip atm, but on fedora it's packaged.
RUN yum upgrade -y && \
    yum install -y epel-release && \
    yum install -y httpd python2-pip && \
    yum clean all && \
    rpm --rebuilddb && \
    /usr/bin/pip2 install tinkerer

# Setup the apache config. This involves changing ports, and disabling a bunch of modules.
RUN chown -R apache: /var/log/httpd && \
    chown -R apache: /var/run/httpd && \
    chmod -R 777 /var/log/httpd && \
    chmod -R 777 /var/run/httpd

COPY 00-base.conf /etc/httpd/conf.modules.d/00-base.conf
COPY httpd.conf /etc/httpd/conf/httpd.conf

# Add the files for the blog.
RUN mkdir -p /srv/
ADD blog_source /srv/

# Now build it out to the apache directory.
WORKDIR /srv/
RUN /usr/bin/tinker --build && \
    ls -al && \
    cp -a {entry,blog,index.html} /var/www/html/

USER apache
CMD ["httpd", "-DFOREGROUND"]

