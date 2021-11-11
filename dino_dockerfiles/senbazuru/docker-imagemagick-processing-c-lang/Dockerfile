FROM centos:centos7
MAINTAINER senbazuru

ENV IMAGEMAGICK_VERSION 6.8.6-10
ENV IMAGEMAGICK_ARCHIVE ImageMagick-$IMAGEMAGICK_VERSION.tar.gz
ENV IMAGEMAGICK_PREFIX /opt/ImageMagick
ENV IMAGEMAGICK_LD_CONF /etc/ld.so.conf.d/imagemagick.conf

RUN yum install -y epel-release
RUN yum update  -y
RUN yum install -y \
    gcc make tar \
    libjpeg-turbo-devel \
    libpng-devel \
    freetype-devel \
    httpd-devel \
    CUnit-devel \
    json-c-devel \
    libcurl-devel \
    openssl-devel \
    glib2-devel \
    gdb 
RUN yum clean all

RUN mkdir -p ${IMAGEMAGICK_PREFIX}/src
WORKDIR ${IMAGEMAGICK_PREFIX}/src 
RUN curl -sL https://raw.githubusercontent.com/senbazuru/imagemagicks/master/$IMAGEMAGICK_ARCHIVE  -o $IMAGEMAGICK_ARCHIVE 
RUN tar zxvf ${IMAGEMAGICK_ARCHIVE} && rm $IMAGEMAGICK_ARCHIVE 
WORKDIR ImageMagick-$IMAGEMAGICK_VERSION 
RUN ./configure --prefix=$IMAGEMAGICK_PREFIX --enable-shared --disable-openmp --disable-opencl --without-x
RUN make && make install 
RUN rm -rf $IMAGEMAGICK_PREFIX/share $IMAGEMAGICK_PREFIX/src

RUN echo $IMAGEMAGICK_PREFIX/lib/ > $IMAGEMAGICK_LD_CONF && ldconfig

ENV PATH /opt/ImageMagick/bin/:$PATH

