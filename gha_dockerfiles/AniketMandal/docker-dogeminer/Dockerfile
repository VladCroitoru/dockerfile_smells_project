FROM tianon/centos
RUN yum install -y gcc make curl-devel wget tar
RUN cd /root/ && wget http://sourceforge.net/projects/cpuminer/files/pooler-cpuminer-2.3.2.tar.gz
RUN cd /root/ && tar xzf pooler-cpuminer-*.tar.gz
RUN cd /root/cpuminer-* && ./configure CFLAGS="-O3"
RUN cd /root/cpuminer-* && make
RUN cd /root/cpuminer-* && make install
// Testing for Hacktober fest
