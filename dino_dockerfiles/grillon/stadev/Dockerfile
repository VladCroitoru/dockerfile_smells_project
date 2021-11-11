# Version 0.0.1
FROM docker.io/grillon/stamain:latest
MAINTAINER Thierry VOGEL <thierry.vogel@moncourriel.eu>
#env de developpement applicatif

#edition
RUN yum -y update 

RUN yum -y install cpanminus expat-devel gcc 

#RUN cpanm --local-lib=~/perl5 local::lib && eval $(perl -I ~/perl5/lib/perl5/ -Mlocal::lib)
RUN yum -y install sbcl emacs nano man ruby ruby-devel perl net-tools libstdc++-doc telnet java-1.8.0-openjdk-devel gdb gcc-c++

RUN yum clean all && rm -Rf /tmp/* /var/tmp/*

EXPOSE 22

#VOLUME /var/log/supervisor
#VOLUME /home

ENTRYPOINT ["/prepare.sh"]
CMD ["ssh"]
