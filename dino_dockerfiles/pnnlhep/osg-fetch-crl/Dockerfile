FROM pnnlhep/osg-base
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

ADD ./start.sh /etc/start.sh
RUN \
  yum install -y http://repo.grid.iu.edu/osg/3.4/osg-3.4-el6-release-latest.rpm; \
  yum clean all; \
  yum install -y fetch-crl crontabs cronie-anacron osg-ca-certs perl-Crypt-SSLeay rsync && \
  mv /etc/grid-security/certificates /etc/grid-security/certificates.orig && \
  touch /var/lock/subsys/fetch-crl-cron && \
  chmod +x /etc/start.sh && \
  sed -i 's/^\(.*pam_loginuid.so\)$/#\1/' /etc/pam.d/crond

CMD ["/etc/start.sh"]
