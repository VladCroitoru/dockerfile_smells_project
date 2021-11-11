FROM centos:centos7

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

# install main packages:
RUN yum -y update; yum clean all;

RUN yum -y install epel-release; yum -y install perl-core; yum -y install perl-App-cpanminus; yum -y install gcc
RUN yum install -y gcc-c++

RUN yum install -y cairo-devel
RUN yum install -y glibc
RUN yum install -y pango-devel
RUN yum install -y gtk2-devel
RUN yum install -y dejavu-lgc-sans-fonts
RUN cpanm Cairo
RUN cpanm Pango
RUN cpanm Glib
RUN cpanm Gtk2
RUN cpanm Template
RUN cpanm Data::Dumper

CMD [ "bash"]

