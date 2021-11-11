FROM centos:latest
MAINTAINER Patrick Dehornoy patrick.dehornoy@unicaen.fr

RUN yum -y update
RUN yum install -y epel-release
RUN yum install -y git 
RUN yum install -y wget
RUN yum install -y emacs nano
RUN yum install -y unzip

RUN wget https://sourceforge.net/projects/lazarus/files/Lazarus%20Linux%20x86_64%20RPM/Lazarus%201.6/fpc-3.0.0-1.x86_64.rpm
RUN rpm -Uvh fpc-3.0.0-1.x86_64.rpm

WORKDIR /workspace
RUN cd /workspace

RUN wget http://www.math.unicaen.fr/~dehornoy/Softwares/MoKaSources.zip
RUN unzip MoKaSources.zip
RUN cd MoKaSources && fpc -Sh MoKa.lpr && cp MoKa /usr/bin/.

RUN wget http://www.math.unicaen.fr/~dehornoy/Softwares/BraidsSources.zip
RUN unzip BraidsSources.zip
RUN cd BraidsSources && fpc -Sh Braids.lpr && cp Braids /usr/bin/.
