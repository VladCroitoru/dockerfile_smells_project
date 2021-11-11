FROM centos:centos5

ARG MAKE_J

RUN rm -f /etc/yum.repos.d/*.repo
ADD CentOS-Vault.repo /etc/yum.repos.d/CentOS-Vault.repo
ADD build.sh /
RUN touch /var/lib/rpm/* &&\
  yum install -y wget &&\
  wget -nv -T 30 -O /etc/yum.repos.d/devtools-2.repo http://people.centos.org/tru/devtools-2/devtools-2.repo &&\
  yum install -y devtoolset-2 make binutils automake autoconf libtool pkgconfig file | tee /yum.log &&\
  scl enable devtoolset-2 /build.sh &&\
  awk '/Dependency Installed:/{f=1;next} /Complete!/{f=0} f' /yum.log | awk -F ' ' '{print $1}' | xargs rpm -e --nodeps &&\
  yum remove -y wget devtoolset-2 make binutils automake autoconf libtool pkgconfig file &&\
  yum clean all &&\
  rm -f /yum.log /etc/yum.repos.d/devtools-2.repo
