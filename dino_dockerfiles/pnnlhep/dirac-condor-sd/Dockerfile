FROM pnnlhep/osg-base
MAINTAINER Malachi Schram "malachi.schram@pnnl.gov"

RUN yum install -y osg-ca-certs osg-ce-condor

ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh

CMD ["/etc/start.sh"]
