FROM centos:centos7

MAINTAINER O. Schacher <oli@fuglu.org>

#### GET DEPENDENCIES

RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y install python-setuptools wget gcc \
  clamav clamav-server clamav-update spamassassin\
  postfix tar python-sqlalchemy python-magic mariadb-devel python-devel 

RUN easy_install supervisor supervisor-stdout syslog-stdout MySQL-python BeautifulSoup

RUN cd /tmp &&\
 wget http://github.com/gryphius/fuglu/tarball/master -O /tmp/fuglu.tar.gz &&\
 tar -xvzf fuglu.tar.gz &&\
 cd *fuglu-*/fuglu/ &&\
 python setup.py install

RUN for file in /etc/fuglu/*.dist; do mv "$file" "/etc/fuglu/`basename -s .dist $file `" ; done

#### UPDATE CONFIG
ADD etc /etc

RUN postconf -e "myorigin = docker.fuglu.org" &&\
  postconf -e "content_filter = fuglu_default:[127.0.0.1]:10025" &&\
  postconf -e "fuglu_default_destination_recipient_limit=1" &&\
  postconf -e "inet_interfaces = all" && \
  postconf -e "myhostname = docker.fuglu.org" &&\
  newaliases && cat /etc/master.cf.additions >> /etc/postfix/master.cf

### FINALIZE SETUP
#needs to be done after new config is in place
RUN adduser clamav && freshclam

#postfix, fuglu
EXPOSE 25 10025 10026 10099

CMD python -u /usr/bin/supervisord
