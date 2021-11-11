FROM centos:7.1.1503

RUN yum install -y bash git autoconf automake shtool libtool gettext glib-devel m4 autogen wget fontconfig-devel make gcc gcc-c++ && \
    wget https://poppler.freedesktop.org/poppler-0.24.5.tar.xz && \
    tar -xf poppler-0.24.5.tar.xz && \
    cd poppler-0.24.5 && ./configure --prefix=/usr "--enable-xpdf-headers" && make && make install && \
    cp /usr/lib/libpoppler.so.44.0.0 /usr/lib64/ && ldconfig
