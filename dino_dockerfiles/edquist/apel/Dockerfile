
FROM opensciencegrid/osg-wn:3.3-el7

# install dependencies
RUN yum -y install --enablerepo=osg-contrib python-elasticsearch-dsl && \
  yum -y install https://github.com/apel/ssm/releases/download/2.1.7-1/apel-ssm-2.1.7-1.el7.noarch.rpm && \
  mkdir /etc/grid-security/apel && \
  mkdir -p /var/spool/apel/outgoing/12345678 && \
  { fetch-crl -p10 -T10 || :; }

COPY apel_report.py normal_hepspec docker-run.sh /usr/libexec/apel/
COPY sender.cfg /etc/apel/

CMD /usr/libexec/apel/docker-run.sh
