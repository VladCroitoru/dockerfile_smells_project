FROM fedora:latest

RUN dnf -y update && dnf -y install wget mingw32-gcc-c++ mingw32-gcc mingw32-gcc-gfortran mingw32-libgomp make doxygen

RUN /bin/bash -c ' \
    wget http://www.fftw.org/fftw-3.3.6-pl2.tar.gz; \
    tar -zxvf fftw-3.3.6-pl2.tar.gz; \
    cd fftw-3.3.6-pl2; \
    ./configure --host='i686-w64-mingw32' --build='x86_64-unknown-linux-gnu' --prefix='/usr/i686-w64-mingw32/sys-root/mingw' --disable-static --enable-shared --enable-threads --with-combined-threads ; \
    make -j $(nproc) bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS= ; \
    make install bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS=  ; \
    '
