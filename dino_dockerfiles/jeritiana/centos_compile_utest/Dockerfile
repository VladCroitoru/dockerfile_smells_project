FROM toopher/centos-i386:centos5
MAINTAINER The U-TEST Team

## Additional installs
# Install wget
COPY wget-1.11.4-3.el5_8.2.i386.rpm /tmp/wget-1.11.4-3.el5_8.2.i386.rpm
RUN rpm -i /tmp/wget-1.11.4-3.el5_8.2.i386.rpm && rm -f /tmp/wget-1.11.4-3.el5_8.2.i386.rpm

# Add EPEL repos
RUN wget --no-check-certificate https://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm -O /tmp/epel-release-5-4.noarch.rpm \
    && rpm -Uvh /tmp/epel-release-5-4.noarch.rpm \
    && rm -f /tmp/epel-release-5-4.noarch.rpm

# Add rpmforge repos from WSU mirror --> for inkscape
RUN wget --no-check-certificate http://repoforge.eecs.wsu.edu/redhat/el5/en/i386/rpmforge/RPMS/rpmforge-release-0.5.3-1.el5.rf.i386.rpm -O /tmp/rpmforge-release-0.5.3-1.el5.rf.i386.rpm \
    && rpm -Uvh /tmp/rpmforge-release-0.5.3-1.el5.rf.i386.rpm \
    && rm -f /tmp/rpmforge-release-0.5.3-1.el5.rf.i386.rpm

# For yum to be able to calculate sha256
RUN linux32 yum install -y python-hashlib

## U-TEST externals
# A working C/C++ compiler for 32/64 bits binaries
RUN linux32 yum install -y gcc-c++ glibc-devel libstdc++-devel libgcc compat-libstdc++-33

# GIT & CMAKE
RUN linux32 yum install -y git make cmake ant wget swig createrepo rpm-build

# Some U-TEST dependancies
RUN linux32 yum install -y postgresql postgresql-server postgresql-odbc unixODBC

# Dependancies for U-TEST Externals
RUN linux32 yum install -y xerces-c-devel ncurses-devel libicu \
                   bzip2-libs openmpi readline \
                   python-libs libpcap-devel unixODBC-devel libxml2-devel \
                   python-devel sqlite-devel openssl-devel keyutils-libs-devel \
                   cppunit-devel java-1.7.0-openjdk-devel

RUN linux32 yum install -y inkscape doxygen

# Explicit upgrade of doxygen
COPY doxygen-1.8.1-3.1.2.i386.rpm /tmp/doxygen-1.8.1-3.1.2.i386.rpm
RUN yum erase -y doxygen
RUN rpm -i /tmp/doxygen-1.8.1-3.1.2.i386.rpm && rm -f /tmp/doxygen-1.8.1-3.1.2.i386.rpm
