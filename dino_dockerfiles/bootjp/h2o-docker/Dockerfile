FROM fedora:22

MAINTAINER oh@bootjp.me

RUN dnf install -y https://bitbucket.org/kjdev/fc22-rpms/raw/master/RPMS/x86_64/kjdev-release-22-1.fc22.kjdev.noarch.rpm https://bitbucket.org/kjdev/fc22-rpms/raw/master/RPMS/x86_64/kjdev-release-scl-22-1.fc22.kjdev.noarch.rpm && dnf clean all
RUN dnf install -y h2o php7-php-cgi php7-php-opcache && dnf clean all

EXPOSE 80 443

ADD ./h2o.conf /etc/h2o/h2o.conf
ADD ./data/ /webapp
ADD ./keys/ /var/tmp/keys/
RUN chown -R root:root /var/tmp/keys/

CMD /usr/bin/h2o -c /etc/h2o/h2o.conf
