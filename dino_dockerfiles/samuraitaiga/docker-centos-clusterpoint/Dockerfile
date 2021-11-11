FROM centos:6
MAINTAINER samuraitaiga

WORKDIR /root

RUN yum install -y tar
RUN curl -L -O http://docs.clusterpoint.com/w/images/c/cd/Centos-cps2-server.x86_64.rpm && yum --nogpgcheck localinstall -y Centos-cps2-server.x86_64.rpm

EXPOSE 5550 5580

ENTRYPOINT ["/usr/local/cps2/cps2_active/server/cps2-master"]
