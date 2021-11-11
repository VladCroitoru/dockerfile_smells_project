FROM centos:centos7
MAINTAINER Amit Bakshi <ambakshi@gmail.com>

RUN yum update -y && yum groupinstall -y 'Development tools' && yum install -y epel-release libpng-devel libjpeg-devel
RUN git clone https://github.com/hglm/libfgen.git /src/libfgen
RUN make -C /src/libfgen install && ldconfig
RUN git clone https://github.com/hglm/texgenpack.git /src/texgenpack
RUN make -C /src/texgenpack texgenpack && install -m 0755 /src/texgenpack/texgenpack /usr/bin/texgenpack
VOLUME /output
ENTRYPOINT ["/usr/bin/texgenpack"]

