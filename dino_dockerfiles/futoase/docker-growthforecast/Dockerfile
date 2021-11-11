FROM centos

MAINTAINER Keiji Matsuzaki <futoase@gmail.com>

# setup network
# reference from https://github.com/dotcloud/docker/issues/1240#issuecomment-21807183
RUN echo "NETWORKING=yes" > /etc/sysconfig/network

# setup remi repository
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN curl -O http://rpms.famillecollet.com/RPM-GPG-KEY-remi; rpm --import RPM-GPG-KEY-remi
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm
RUN yum -y update
RUN yum -y upgrade

# install sshd, passwd
RUN yum -y install openssh-server passwd
# Change UsePAM yes to no
RUN sed -i -e 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

# setup nginx repository
ADD ./template/nginx.repo /etc/yum.repos.d/nginx.repo

# setup tools
# reference from http://blog.nomadscafe.jp/2013/12/centos-65dockergrowthforecast.html
RUN yum -y groupinstall --enablerepo=epel,remi "Development Tools"
RUN yum -y install --enablerepo=epel,remi pkgconfig glib2-devel gettext libxml2-devel pango-devel cairo-devel git ipa-gothic-fonts
RUN yum -y install --enablerepo=epel,remi mysql mysql-server mysql-devel

# install nginx
RUN yum -y install --enablerepo=nginx nginx

# install supervisor
RUN yum -y install --enablerepo=epel,remi supervisor

# setup perlbrew
RUN export PERLBREW_ROOT=/opt/perlbrew && curl -L http://install.perlbrew.pl | bash
RUN source /opt/perlbrew/etc/bashrc && perlbrew install perl-5.18.2
RUN source /opt/perlbrew/etc/bashrc && perlbrew use perl-5.18.2 && perlbrew install-cpanm

# create growthforecast user
RUN useradd -m growthforecast
RUN echo "growthforecast" | passwd --stdin growthforecast

# create directories
RUN mkdir -p /home/growthforecast/scripts && chown growthforecast:growthforecast /home/growthforecast/scripts
RUN mkdir -p /home/growthforecast/data && chown growthforecast:growthforecast /home/growthforecast/data

RUN git clone https://github.com/kazeburo/GrowthForecast.git /home/growthforecast/GrowthForecast.git
RUN mkdir -p /var/nginx/GRF && chown nginx:nginx /var/nginx/GRF
RUN cp -aR /home/growthforecast/GrowthForecast.git/public /var/nginx/GRF
RUN chown -R nginx:nginx /var/nginx/GRF/public

# setup mysql
ADD ./scripts/mysqld-setup.sh /home/growthforecast/scripts/mysqld-setup.sh
RUN chmod +x /home/growthforecast/scripts/mysqld-setup.sh
RUN /home/growthforecast/scripts/mysqld-setup.sh

# setup nginx
ADD ./template/nginx.conf /etc/nginx/conf.d/growthforecast.conf
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/conf.d/example_ssl.conf
RUN service nginx restart

# install growthforecast
RUN source /opt/perlbrew/etc/bashrc && perlbrew use perl-5.18.2 && cpanm -n GrowthForecast
RUN source /opt/perlbrew/etc/bashrc && perlbrew use perl-5.18.2 && cpanm -n DBD::mysql

# setup supervisor
RUN sed -i -e "s/nodaemon=false/nodaemon=true/g" /etc/supervisord.conf
ADD ./template/supervisor.conf /tmp/growthforecast.conf
RUN cat /tmp/growthforecast.conf >> /etc/supervisord.conf
RUN rm /tmp/growthforecast.conf

# startup
ENV PATH /opt/perlbrew/perls/perl-5.18.2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# setup for mysql connection environment variable.
ENV MYSQL_USER growthforecast
ENV MYSQL_PASSWORD growthforecast

ADD ./scripts/timezone.sh /home/growthforecast/scripts/timezone.sh
RUN chmod +x /home/growthforecast/scripts/timezone.sh
ADD ./scripts/startup.sh /home/growthforecast/scripts/startup.sh
RUN chmod +x /home/growthforecast/scripts/startup.sh

EXPOSE 22 80
CMD ["/home/growthforecast/scripts/startup.sh"]
