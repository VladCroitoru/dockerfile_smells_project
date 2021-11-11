FROM centos:centos6

# Install the prereqs
RUN yum -y install sudo httpd mod_perl make net-snmp net-snmp-utils tar wget which

# Because GD is gd everywhere
RUN yum -y install gd gd-devel

# Because there are RPMs for more perl modules here
RUN rpm -Uvh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm

# Install perl bits because... sigh
RUN yum -y install perl-Net-IP perl-DBI perl-DBD-mysql perl-DateManip net-snmp-perl perl-Date-Calc perl-TimeDate perl-MailTools perl-Net-DNS perl-Time-HiRes perl-CGI perl-GDGraph perl-Text-Diff perl-OLE-Storage_Lite perl-Spreadsheet-ParseExcel perl-Parallel-ForkManager perl-Net-Ping-External

# Because there has to be a straggler because perl
RUN rpm -Uvh http://mirrors.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm

# ...and straggler
RUN yum -y install perl-SNMP-Info; yum clean all

# clean up after ourselves
RUN yum clean all

# Setup httpd users
RUN if [ ! -f /root/.gestiooper ]; then echo $(/usr/bin/tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1) > /root/.gestiooper; fi
RUN chmod 0600 /root/.gestiooper
RUN if [ ! -f /root/.gestioadmin ]; then echo $(/usr/bin/tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1) > /root/.gestioadmin; fi
RUN chmod 0600 /root/.gestioadmin
RUN if [ ! -f /etc/httpd/users-gestioip ]; then /usr/bin/htpasswd -b -c /etc/httpd/users-gestioip gipoper $(cat /root/.gestiooper); fi
RUN if [ ! -f /etc/httpd/users-gestioip ]; then /usr/bin/htpasswd -b /etc/httpd/users-gestioip gipadmin $(cat /root/.gestioadmin); fi

# Download gestioip itself
RUN curl -L -o gestioip_3.0.tar.gz 'http://downloads.sourceforge.net/project/gestioip/gestioip_3.0.tar.gz?r=http%3A%2F%2Fwww.gestioip.net%2F&ts=1403922795&use_mirror=hivelocity'

RUN tar xzvf gestioip_3.0.tar.gz

# Download, unpack and netdisco mibs
RUN curl -L -o netdisco-mibs-snapshot.tar.gz 'http://downloads.sourceforge.net/project/netdisco/netdisco-mibs/latest-snapshot/netdisco-mibs-snapshot.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnetdisco%2Ffiles%2Fnetdisco-mibs%2Flatest-snapshot%2F&ts=1404795738&use_mirror=superb-dca3'
RUN tar xzvf netdisco-mibs-snapshot.tar.gz
RUN mkdir -p /usr/share/gestioip
RUN chown apache:apache /usr/share/gestioip
RUN mv netdisco-mibs /usr/share/gestioip/mibs

# Expose some ports
EXPOSE 80

#Borrowed from fedora/apache but it's docker build was broken
#https://github.com/fedora-cloud/Fedora-Dockerfiles/blob/master/apache/Dockerfile
# Simple startup script to avoid some issues observed with container restart
ADD run-apache.sh /run-apache.sh
RUN chmod -v +x /run-apache.sh

CMD ["/run-apache.sh"]
