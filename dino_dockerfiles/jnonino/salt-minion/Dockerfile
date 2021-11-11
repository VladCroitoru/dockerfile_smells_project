FROM centos:7
LABEL maintainer="Julian Nonino <noninojulian@gmail.com>"

RUN yum update --assumeyes && \
    yum install --assumeyes epel-release initscripts python2 && \
    yum install --assumeyes https://repo.saltstack.com/yum/redhat/salt-repo-latest-2.el7.noarch.rpm && \
    yum clean expire-cache && \
    yum install --assumeyes salt-minion && \
    yum clean all && \
    rm -rf /var/cache/yum


# Overwrite the default tcp ports used by the minion when in tcp mode
#tcp_pub_port: 4510
#tcp_pull_port: 4511

COPY start.sh /usr/local/bin
ENTRYPOINT [ "/usr/local/bin/start.sh" ]