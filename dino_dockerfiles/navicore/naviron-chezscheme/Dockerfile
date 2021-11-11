FROM navicore/naviron-other

MAINTAINER Ed Sweeney <ed@onextent.com>

WORKDIR /root

RUN yum -y install xorg-x11-server-devel \
    && wget -q https://github.com/cisco/ChezScheme/archive/v9.5.tar.gz && tar zxf v9.5.tar.gz && cd ChezScheme-9.5 && ./configure && make install && cd .. && rm -rf ChezSche*

