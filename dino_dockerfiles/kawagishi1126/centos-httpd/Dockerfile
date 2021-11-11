FROM centos:7

# Install httpd
RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install less vim-minimal which iproute tcpdump httpd openssh-server && \
    yum clean all
EXPOSE 2222 80


# Simple startup script to avoid some issues observed with container restart
COPY run-webapponlinux-httpd.sh /usr/local/bin/
RUN cp -ip /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.org
#COPY httpd.conf /etc/httpd/conf/httpd.conf.tmp
COPY httpd.conf /etc/httpd/conf/
COPY sshd_config /etc/ssh/
RUN ssh-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key

ENV SSH_PASSWD "root:Docker!"
RUN echo "$SSH_PASSWD" | chpasswd
RUN chmod -v +x /usr/local/bin/run-webapponlinux-httpd.sh
CMD ["/usr/local/bin/run-webapponlinux-httpd.sh"]
