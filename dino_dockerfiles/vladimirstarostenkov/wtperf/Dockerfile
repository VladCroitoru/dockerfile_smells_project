FROM centos:7

RUN yum group install -y "Development Tools" \
 && git clone git://github.com/wiredtiger/wiredtiger.git \
 && cd wiredtiger \
 && ./autogen.sh \
 && ./configure \
 && make

ENTRYPOINT ["/wiredtiger/bench/wtperf/wtperf"]
