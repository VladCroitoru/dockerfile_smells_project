FROM centos:7
MAINTAINER "Pavel Studenik" <pstudeni@redhat.com>

# download and install spacewalk nightly client repository
RUN URL_SW=http://yum.spacewalkproject.org/2.7-client/RHEL/7/x86_64/ && \
    rpm -Uvh $URL_SW/$( curl --silent $URL_SW | grep spacewalk-client-repo-[0-9] |  grep -Po '(?<=href=")[^"]*' ) && \
    curl http://yum.spacewalkproject.org/RPM-GPG-KEY-spacewalk-2015 > RPM-GPG-KEY-spacewalk-2015 && \
    rpm --import RPM-GPG-KEY-spacewalk-2015 && \
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

# enable nightly repository and disable others
#RUN sed s/enabled=0/enabled=1/g /etc/yum.repos.d/spacewalk-client-nightly.repo -i && \
#    sed s/enabled=1/enabled=0/g /etc/yum.repos.d/spacewalk-client.repo -i

RUN yum install -y rhn-client-tools rhn-check rhn-setup rhnsd hwdata m2crypto wget osad rhncfg-*

ADD bin/register.sh /root/register.sh
ADD bin/osad.sh /root/osad.sh

RUN chmod a+x /root/{register.sh,osad.sh}

CMD /root/osad.sh

