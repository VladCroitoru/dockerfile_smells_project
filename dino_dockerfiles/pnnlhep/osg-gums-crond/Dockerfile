FROM pnnlhep/osg-base
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

RUN yum install -y gums-client crontabs cronie-anacron
RUN touch /var/lock/subsys/gums-host-cron
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh
RUN sed -i 's/^\(.*pam_loginuid.so\)$/#\1/' /etc/pam.d/crond

CMD ["/etc/start.sh"]
