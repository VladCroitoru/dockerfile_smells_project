FROM pnnlhep/osg-compute
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

ADD ./fts3.repo /etc/yum.repos.d/fts3.repo
ADD ./liberty.repo /etc/yum.repos.d/liberty.repo
RUN rpm -Uvh http://software.internet2.edu/rpms/el6/x86_64/main/RPMS/Internet2-repo-0.6-1.noarch.rpm

#Rebuild manpages
RUN [ -e /etc/yum.conf ] && sed -i '/tsflags=nodocs/d' /etc/yum.conf || true; \
    yum -y reinstall --exclude=filesystem "*"

RUN yum clean all; yum install -y sysstat bwctl-client strace bzip2-devel openssl-devel ncurses-devel readline-devel screen telnet zsh gdb git osg-client osg-client-condor edg-mkgridmap lcmaps-plugins-gums-client lcmaps-plugins-basic lcmaps-plugins-verify-proxy fts-client voms-admin-client python-heatclient python-cinderclient python-novaclient python-neutronclient openssh-server ansible lsof vim-enhanced strace gdb man nc emacs xemacs byobu xauth 389-console pam_ldap; \
    rpm -Uvh https://packages.chef.io/stable/el/6/chefdk-1.4.3-1.el6.x86_64.rpm

ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh
ADD ./drain.sh /etc/drain.sh
RUN chmod +x /etc/drain.sh

CMD ["/etc/start.sh"]
