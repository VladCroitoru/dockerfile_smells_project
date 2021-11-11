FROM centos:7

EXPOSE 80
ENTRYPOINT [ "/init" ]

ENV SMOKEPING_VERSION 2.6.10

# install packages
RUN yum -y install epel-release \
        && yum -y install \
            httpd \
            postfix \
            smokeping-${SMOKEPING_VERSION} \
            supervisor \
        && yum -y clean all

# install operating system configuration
COPY docker/ /
