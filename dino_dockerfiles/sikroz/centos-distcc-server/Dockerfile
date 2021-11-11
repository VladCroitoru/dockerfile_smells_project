FROM sikroz/centos-build
MAINTAINER sikroz
RUN yum install -y distcc-server; yum clean all
EXPOSE 3632
CMD ["distccd", "--no-detach", "--log-stderr", "--verbose", "-a", "0.0.0.0/0"]
