FROM sigtom/docker-cent6ssh
MAINTAINER "Tommy Craddock" <tec.thor@gmail.com>

#Install EPEL Repo
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -ivh epel-release-6-8.noarch.rpm
COPY files/epel.repo /etc/yum.repos.d

#Install prereqs for cobbler, koan, and cobbler-web
RUN yum -y install createrepo httpd mkisofs mod_wsgi mod_ssl python-cheetah python-netaddr python-simplejson PyYAML rsync syslinux tftp-server yum-utils Django python-simplejson git python-devel python-setuptools python-cheetah

#Install Cobbler
RUN yum -y install cobbler cobbler-web dnsmasq syslinux pykickstart debmirror

# create rsync file
#COPY files/rsync /etc/xinetd.d
COPY files/dnsmasq.template /etc/cobbler
COPY files/settings /etc/cobbler
COPY files/modules.conf /etc/cobbler
COPY files/debmirror.conf /etc

# enable tftp and rsync
RUN sed -i -e 's/\(^.*disable.*=\) yes/\1 no/' /etc/xinetd.d/tftp
RUN sed -i -e 's/\(^.*disable.*=\) yes/\1 no/' /etc/xinetd.d/rsync
RUN sed -i.orig "s/#ServerName www.example.com:80/ServerName $HOSTNAME/g" /etc/httpd/conf/httpd.conf

#yYum update
RUN yum clean all; yum -y update

RUN service cobblerd start
RUN service httpd start
#RUN service dnsmasq start
RUN service xinetd start
RUN chkconfig cobblerd on
RUN chkconfig httpd on
RUN chkconfig dnsmasq on
RUN chkconfig xinetd on

# solve "dnsmasq: setting capabilities failed: Operation not permitted"
# refs:https://github.com/nicolasff/docker-cassandra/issues/8
RUN echo "user=root" >> /etc/dnsmasq.conf
RUN service dnsmasq start
RUN cat /etc/httpd/conf/httpd.conf | grep ServerName
RUN updatedb

EXPOSE 22
EXPOSE 69
EXPOSE 80
EXPOSE 25151
EXPOSE 873
Expose 443
CMD ["/bin/bash"]
