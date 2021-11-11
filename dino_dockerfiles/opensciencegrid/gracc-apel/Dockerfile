FROM opensciencegrid/osg-wn:3.5-el7

# install dependencies
RUN yum -y install python3 python3-pip && \
  pip3 install elasticsearch-dsl && \
  pip3 install argo-ams-library
RUN yum -y install http://rpm-repo.argo.grnet.gr/ARGO/devel/centos7/python-argo-ams-library-0.5.5-20210415071520.ff0c536.el7.noarch.rpm

RUN yum -y install python-dirq

# install ca-policy-egi-core
RUN yum -y remove osg-ca-certs
RUN cd /etc/yum.repos.d/ && \
  wget http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-trustanchors.repo && \
  yum -y install ca-policy-egi-core


RUN yum -y install https://github.com/apel/ssm/releases/download/3.2.1-1/apel-ssm-3.2.1-1.el7.noarch.rpm  && \
  mkdir /etc/grid-security/apel && \
  mkdir -p /var/spool/apel/outgoing/12345678 && \
  { fetch-crl -p10 -T10 || :; }

COPY apel_report.py normal_hepspec docker-run.sh /usr/libexec/apel/
COPY sender.cfg /etc/apel/

ENTRYPOINT ["/usr/libexec/apel/docker-run.sh"]
