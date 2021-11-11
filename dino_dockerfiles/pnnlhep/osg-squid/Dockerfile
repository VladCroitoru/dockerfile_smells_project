FROM pnnlhep/osg-base
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

RUN yum install -y squid
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh

CMD ["/etc/start.sh"]
