FROM centos:centos7

RUN yum -y update && yum -y groupinstall 'Development Tools' && yum -y install gsl gsl-devel autoconf ant texinfo kernel zlib-devel kernel-devel httpd wget

RUN wget http://repository.it4i.cz/mirrors/repoforge/redhat/el7/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm && rpm -i rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm

RUN yum -y update &&  yum -y install p7zip p7zip-plugins which

RUN mkdir -p /usr/local/share/man/man1 && git clone https://github.com/pjmaker/nana.git && cd nana && autoreconf --install && ./configure && make && make install && cd .. && rm -rf nana

RUN wget http://ftp.gnu.org/gnu/cgicc/cgicc-3.2.19.tar.gz && tar -xvf cgicc-3.2.19.tar.gz && cd cgicc-3.2.19 && ./configure && make && make install && cd .. && rm -rf cgicc-3.2.19

