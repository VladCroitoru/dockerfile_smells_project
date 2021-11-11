FROM centos:8

# MAINTAINER Emmanuel Mathot <emmanuel.mathot@terradue.com>

RUN yum install -y epel-release unzip procps \
    && curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v latest -l /vsdbg
ARG STARS_RPM
COPY $STARS_RPM /tmp/$STARS_RPM
RUN yum localinstall -y /tmp/$STARS_RPM