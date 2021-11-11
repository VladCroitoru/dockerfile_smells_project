FROM openshift/origin-base:latest
MAINTAINER Daniel Tschan <tschan@puzzle.ch>

RUN yum -y install docker-1.8.2 docker-selinux-1.8.2 subversion; yum clean all

ADD ./build.sh /tmp/build.sh

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/tmp/build.sh"]
