FROM centos
MAINTAINER KUNIYOSHI kouji <kuniyoshi.kouji@gmail.com>

RUN yum clean all && yum -y update
RUN yum install -y git ant gij

RUN mkdir /opt/yui-compressor
WORKDIR /opt/yui-compressor

RUN git clone git://github.com/yui/yuicompressor.git \
    && cd yuicompressor \
    && git checkout -b yuicompressor-24 \
    && ant

RUN mkdir /opt/yui-compressor/public
WORKDIR /opt/yui-compressor/public

RUN useradd -d /dev/null -M -r -s /sbin/nologin yuicompressor
RUN chown -R yuicompressor:yuicompressor .
USER yuicompressor

ENTRYPOINT ["java", "-jar", "/opt/yui-compressor/yuicompressor/build/yuicompressor-2.4.8.jar"]
CMD ["--help"]
