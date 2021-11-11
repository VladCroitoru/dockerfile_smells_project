FROM centos:7
MAINTAINER "Niels Vandekeybus" <progster@gmail.com>
RUN yum -y update && yum -y install git gcc gmake autoconf net-tools automake libtool flex openssl bison gperf gawk m4 make openssl-devel readline-devel wget rpm-build redhat-rpm-config  &&  useradd rpmbuild && mkdir -p /home/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} && echo '%_topdir /home/rpmbuild' > /home/rpmbuild/.rpmmacros && git clone https://github.com/openlink/virtuoso-opensource.git /home/rpmbuild/virtuoso-opensource
ADD SPECS/virtuoso-opensource.spec /home/rpmbuild/SPECS/
ADD build-rpm.sh /home/rpmbuild/
ADD tf-addons/ /home/rpmbuild/virtuoso-opensource/tf-addons
RUN chown rpmbuild -R /home/rpmbuild && chmod +x /home/rpmbuild/build-rpm.sh
VOLUME /home/rpmbuild/RPMS
ENTRYPOINT su rpmbuild -l -c "export VIRT_BRANCH && /home/rpmbuild/build-rpm.sh"