FROM centos:6
MAINTAINER Jeroen van Rhee <jeroen_van_rhee@hotmail.com>

ENV PERL5LIB=/usr/lib/perl5/site_perl/5.10.0

ADD Radiator-4.8-1.noarch.rpm /var/tmp

RUN  yum install -y /var/tmp/Radiator-4.8-1.noarch.rpm && \
     yum install -y perl-DBI perl-DBD-MySQL
            
CMD /usr/bin/radiusd -config_file /etc/radiator/radius.cfg -foreground


