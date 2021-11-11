FROM centos:7
ADD . /inception
RUN yum -y install make cmake gcc gcc-c++ libncurses5-dev libssl-devg++  openssl-devel.x86_64 ncurses-devel
RUN yum  remove bison -y
RUN curl -L http://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.gz -o m4-1.4.18.tar.gz && tar -zxvf m4-1.4.18.tar.gz&& cd m4-1.4.18 && ./configure && make && make install && rm -rf m4-1.4.18.tar.gz  m4-1.4.18
RUN curl -L http://ftp.gnu.org/gnu/bison/bison-2.4.tar.gz -o bison-2.4.tar.gz && tar -zxvf bison-2.4.tar.gz&& cd bison-2.4 && ./configure && make && make install && rm -rf bison-2.4.tar.gz bison-2.4
RUN cd /inception && sh inception_build.sh debug && cp /inception/debug/sql/Inception /bin && rm -rf /inception
ENTRYPOINT ["/bin/Inception"]
EXPOSE 3306
