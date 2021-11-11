FROM ubuntu:16.04
WORKDIR /myapp
RUN apt-get update && \
    apt-get install -y wget gcc make libkrb5-3 libgss3 && \
    wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.1.tar.gz && \
    tar zxf unixODBC-2.3.1.tar.gz && \
    cd unixODBC-2.3.1 && \
    export CPPFLAGS="-DSIZEOF_LONG_INT=8" && \
    ./configure --enable-gui=no --enable-drivers=no --enable-iconv --with-iconv-char-enc=UTF8 --with-iconv-ucode-enc=UTF16LE --libdir=/usr/lib64 --prefix=/usr --sysconfdir=/etc && \
    make && make install && \
    locale-gen "en_US.UTF-8" && \
    echo "/usr/lib64" > /etc/ld.so.conf.d/libodbc.conf && \
    wget https://download.microsoft.com/download/2/E/5/2E58F097-805C-4AB8-9FC6-71288AB4409D/msodbcsql-13.0.0.0.tar.gz && \
    tar zxf msodbcsql-13.0.0.0.tar.gz && \
    cd msodbcsql-13.0.0.0 && \
    ./install.sh install --accept-license && \
    ldconfig && \
    apt-get remove -y gcc && apt-get autoremove -y && \
    apt-get clean && apt-get autoclean

ENV LANG "en_US.UTF-8"
ENTRYPOINT ["sqlcmd"]
