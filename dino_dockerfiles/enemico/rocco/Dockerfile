FROM centos:7

RUN yum -y update

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y yum-utils epel-release
RUN yum install -y git make cmake gcc gcc-c++ libstdc++-static libuv-static hwloc-devel openssl-devel

RUN rm -f /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Oslo /etc/localtime
RUN useradd -ms /usr/bin/bash rocco

COPY ./service /home/rocco/service
RUN chown -R rocco:rocco /home/rocco/service

USER rocco
WORKDIR /home/rocco

RUN git clone https://github.com/xmrig/xmrig.git
RUN mkdir /home/rocco/xmrig/build
COPY ./service/donate.h /home/rocco/xmrig/src/
RUN cd /home/rocco/xmrig/build && cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a -DWITH_HTTPD=OFF
RUN cd /home/rocco/xmrig/build && make

ENTRYPOINT ["/home/rocco/service/start.sh"]
