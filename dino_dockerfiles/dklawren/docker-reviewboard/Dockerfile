FROM centos
MAINTAINER dkl

# Global configuration
ENV RB_USER reviewboard

# Packages
RUN yum -y install https://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
RUN yum -y install https://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN yum -y update
ADD rpm_list /rpm_list
RUN yum -y install `cat /rpm_list`
RUN yum clean all

# User creation
RUN useradd -m -G wheel -u 1000 -s /bin/bash $RB_USER
RUN passwd -u -f $RB_USER
RUN echo "$RB_USER:$RB_USER" | chpasswd
RUN mkdir -p /home/$RB_USER/devel/htdocs

# MySQL configuration
ADD my.cnf /etc/my.cnf
RUN chmod 644 /etc/my.cnf; chown root.root /etc/my.cnf
ADD mysql_config.sh /
RUN chmod 755 /mysql_config.sh
RUN /mysql_config.sh

# Apache configuration
ADD reviewboard.conf /etc/httpd/conf.d/reviewboard.conf
RUN sed -ri "s/User apache/User $RB_USER/" /etc/httpd/conf/httpd.conf
RUN sed -ri "s/Group apache/Group $RB_USER/" /etc/httpd/conf/httpd.conf

# Sshd configuration
ADD ssh_config.sh /ssh_config.sh
RUN chmod 755 /ssh_config.sh
RUN /ssh_config.sh

# Sudo configuration
ADD sudoers /etc/sudoers
RUN chown root.root /etc/sudoers; chmod 440 /etc/sudoers

# Reviewboard configuration
ADD reviewboard_config.sh /reviewboard_config.sh
RUN chmod 755 /reviewboard_config.sh
RUN /reviewboard_config.sh

# Final permissions fix
RUN chown -R $RB_USER.$RB_USER /home/$RB_USER

RUN echo "NETWORKING=yes" > /etc/sysconfig/network
EXPOSE 80 22

# Supervisor
ADD supervisord.conf /etc/supervisord.conf
RUN chmod 700 /etc/supervisord.conf
CMD ["/usr/bin/supervisord"]
