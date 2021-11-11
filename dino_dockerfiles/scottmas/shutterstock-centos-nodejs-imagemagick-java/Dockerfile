FROM centos:7.2.1511

RUN yum update -y
RUN yum install -y git
RUN yum install -y gcc-c++ make
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash -
RUN yum install -y nodejs
RUN yum install -y java-1.8.0-openjdk
RUN yum install -y ghostscript
RUN yum install -y ImageMagick-c++ ImageMagick-c++-devel
RUN yum install -y which

