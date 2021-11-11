#
# Dockerfile - docker build script for a standard GlueX sim-recon 
#              container image based on centos 7.
#
# author: richard.t.jones at uconn.edu
# version: june 7, 2017
# updated: june 13, 2020 
#
# usage: [as root] $ docker build Dockerfile .
#

FROM centos:7

# install a few utility rpms
RUN yum -y install bind-utils util-linux which wget tar procps less file dump gcc gcc-c++ gcc-gfortran gdb gdb-gdbserver strace openssh-server
RUN yum -y install vim-common vim-filesystem docker-io-vim vim-minimal vim-enhanced vim-X11
RUN yum -y install qt qt-x11 qt-devel
RUN yum -y install motif-devel libXpm-devel libXmu-devel libXp-devel
RUN yum -y install java-1.8.0-openjdk
RUN yum -y install blas lapack
RUN yum -y install python3 python3-devel python3-pip
RUN yum -y install postgresql-devel
RUN wget --no-check-certificate https://zeus.phys.uconn.edu/halld/gridwork/libtbb.tgz
RUN tar xf libtbb.tgz -C /
RUN rm libtbb.tgz

# install the osg worker node client packages
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# work-around for problems using the EPEL mirrors (repomd.xml does not match metalink for epel)
RUN sed -i 's/^#baseurl/baseurl/' /etc/yum.repos.d/epel.repo
RUN sed -i 's/^metalink/#metalink/' /etc/yum.repos.d/epel.repo
# end of work-around
RUN yum -y install yum-plugin-priorities
RUN rpm -Uvh https://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm
RUN yum -y install osg-wn-client
RUN wget --no-check-certificate https://zeus.phys.uconn.edu/halld/gridwork/dcache-srmclient-3.0.11-1.noarch.rpm
RUN rpm -Uvh dcache-srmclient-3.0.11-1.noarch.rpm
RUN rm dcache-srmclient-3.0.11-1.noarch.rpm

# install the hdpm package builder
ENV GLUEX_TOP /usr/local
ADD https://halldweb.jlab.org/dist/hdpm/hdpm-0.7.2.linux.tar.gz /
RUN tar xf hdpm-0.7.2.linux.tar.gz
RUN rm hdpm-0.7.2.linux.tar.gz
RUN mv hdpm-0.7.2 hdpm

# install some additional packages that might be useful
RUN yum -y install apr apr-util atlas autoconf automake bc cmake cmake3 git scons bzip2-devel boost-python36
RUN yum -y install gsl gsl-devel libgnome-keyring lyx-fonts m4 neon pakchois mariadb mariadb-libs mariadb-devel
RUN yum -y install perl-File-Slurp perl-Test-Harness perl-Thread-Queue perl-XML-NamespaceSupport perl-XML-Parser perl-XML-SAX perl-XML-SAX-Base perl-XML-Simple perl-XML-Writer
RUN yum -y install subversion subversion-libs
RUN yum -y install python2-pip python-devel
RUN yum -y install hdf5 hdf5-devel
RUN yum -y install valgrind
RUN pip2 install future numpy==1.16.6
RUN pip3 install psycopg2
RUN pip3 install --upgrade pip
RUN python3 -m pip install numpy==1.19.5

# add scl devtoolsets for more advanced compiler options 
RUN yum install -y centos-release-scl centos-release-scl-rh
RUN yum install -y devtoolset-7-gcc-c++ devtoolset-7-gcc-gfortran devtoolset-7-binutils devtoolset-7-gcc-gdb-plugin devtoolset-7-libstdc++-devel devtoolset-7-gcc-plugin-devel
RUN yum install -y devtoolset-8-gcc-c++ devtoolset-8-gcc-gfortran devtoolset-8-binutils devtoolset-8-gcc-gdb-plugin devtoolset-8-libstdc++-devel devtoolset-8-gcc-plugin-devel
RUN yum install -y devtoolset-9-gcc-c++ devtoolset-9-gcc-gfortran devtoolset-9-binutils devtoolset-9-gcc-gdb-plugin devtoolset-9-libstdc++-devel devtoolset-9-gcc-plugin-devel

# create mount point for sim-recon, simlinks in /usr/local
RUN wget --no-check-certificate https://zeus.phys.uconn.edu/halld/gridwork/localtest.tar.gz
RUN mv /usr/sbin/sshd /usr/sbin/sshd_orig
RUN tar xf localtest.tar.gz -C /
RUN rm localtest.tar.gz
RUN rm -rf /hdpm

# make the cvmfs filesystem visible inside the container
VOLUME /cvmfs/oasis.opensciencegrid.org

# set the default build for sim_recon
RUN ln -s /cvmfs/oasis.opensciencegrid.org/gluex/.hdpm /usr/local/
