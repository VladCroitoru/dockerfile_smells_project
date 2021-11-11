# Dockerfile for KDB on centos7
# License BSD, see LICENSE for details

#Build with: sudo docker build -t richardgill/centos-kdb .
#Test with: sudo docker run -i -t richardgill/centos-kdb bash -l

FROM centos:centos7

ENV KDB_VERSION 3.1-2014.08.22

RUN yum install -y rpm-build

RUN yum install -y wget

RUN yum install -y git

#32Bit KDB requires glibc.i686
RUN yum install -y glibc.i686

RUN git clone https://github.com/jasraj/q-build.git /tmp/q-build

RUN wget -P /tmp/ http://kx.com/347_d0szre-fr8917_llrsT4Yle-5839sdX/3.1/linux.zip

RUN unzip -d /tmp /tmp/linux.zip

RUN /tmp/q-build/rpm/build.sh $KDB_VERSION /tmp/q /tmp/rpm-output

RUN rpm -i /tmp/rpm-output/RPMS/x86_64/kdb-plus-$KDB_VERSION.x86_64.rpm
