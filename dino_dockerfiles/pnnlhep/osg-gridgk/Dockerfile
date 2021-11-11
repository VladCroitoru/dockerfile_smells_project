FROM pnnlhep/osg-base
MAINTAINER Malachi Schram "malachi.schram@pnnl.gov"

RUN yum install -y centos-release-SCL
RUN yum install -y xfsprogs python27
RUN yum install -y osg-ca-certs  osg-ce-condor
RUN yum install -y git readline-devel bzip2-devel zlib-devel ncurses-devel openssl-devel
RUN yum install -y fontconfig libxml2 openssl098e libGLU libXpm binutils-devel gcc libgfortran python-devel subversion gcc-gfortran gcc-c++ binutils binutils-devel python-devel libxml2-devel mesa-libGL-devel glew-devel libX11-devel libXpm-devel libXft-devel libXext-devel glew 
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh

CMD ["/etc/start.sh"]
