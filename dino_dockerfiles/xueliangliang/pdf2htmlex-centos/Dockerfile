FROM centos:latest


RUN alias g++="g++ -std=c++11" && \
    alias c++="c++ -std=c++11" && \
    alias cc="cc -std=c++11" && \
    alias && \
    yum install -y git gcc gcc-c++ java-1.8.0-openjdk libxml2-devel patch xz gettext poppler-devel pango-devel m4 libtool libtool-ltdl libtool-ltdl-devel perl autoconf automake make coreutils python-devel zlib-devel freetype-devel glib-devel cmake && \
    cd / && \
    git clone https://github.com/fontforge/fontforge.git && \
    cd fontforge && \
    ./bootstrap --force && \
    ./configure --without-iconv && \
    make && \
    make install && \
    cd / && \
    git clone -b incoming git://github.com/coolwanglu/pdf2htmlEX.git && \
    cd pdf2htmlEX && \
    export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig && \
    cmake . && make && make install && \
    rm -rf /fontforge /pdf2htmlEX 

VOLUME /pdf
WORKDIR /pdf

ENV LD_LIBRARY_PATH "/usr/local/lib"

CMD ["/usr/local/bin/pdf2htmlEX"]
