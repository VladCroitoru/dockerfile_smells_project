FROM centos:7

# Needed to run vespa
RUN yum-config-manager --add-repo https://copr.fedorainfracloud.org/coprs/g/vespa/vespa/repo/epel-7/group_vespa-vespa-epel-7.repo && \
    yum -y install epel-release && \
    yum -y install centos-release-scl 

ADD start-container.sh /usr/local/bin/start-container.sh 

RUN yum install -y vespa-cppunit-1.12.1

ENTRYPOINT ["/usr/local/bin/start-container.sh"]
