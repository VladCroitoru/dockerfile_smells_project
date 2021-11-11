FROM fedora:27

RUN dnf clean metadata

RUN dnf -y --nogpgcheck update; exit 0

RUN dnf -y install cmake git mingw32-qt5* mingw32-gcc-c++ mingw32-gcc mingw32-gcc-gfortran mingw32-libgomp mingw32-gsl mingw32-zlib mingw32-nsis unzip wget autoconf automake bash bison bzip2 flex gcc-c++ gdk-pixbuf2-devel gettext git gperf intltool make sed libffi-devel libtool openssl-devel p7zip patch perl pkgconfig python ruby scons unzip wget xz gtk-doc dh-autoreconf mingw32-portablexdr pandoc 

RUN dnf -y install fedora-repos-rawhide
RUN dnf -y --disablerepo=* --enablerepo=rawhide --releasever=28 install mingw32-python2 mingw32-python2-numpy mingw32-cfitsio

#fftw mingw32-fftw
RUN /bin/bash -c ' mkdir fftw3 && cd fftw3;\
    wget http://www.fftw.org/fftw-3.3.6-pl2.tar.gz;\
    tar -zxvf fftw-3.3.6-pl2.tar.gz; \
    cd fftw-3.3.6-pl2; \
    mingw32-configure --disable-static --enable-shared  ac_cv_prog_HAVE_DOXYGEN="false" --enable-threads --with-combined-threads ; \
    make -j $(nproc) bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS=    ;\
    make install bin_PROGRAMS= sbin_PROGRAMS= noinst_PROGRAMS=   '

#hdf4
RUN wget https://support.hdfgroup.org/ftp/HDF/releases/HDF4.2.10/src/hdf-4.2.10.tar.bz2 && tar -jxvf hdf-4.2.10.tar.bz2; \
    cd hdf-4.2.10; \
    wget https://raw.githubusercontent.com/iltommi/mxe/master/src/hdf4-1-portability-fixes.patch; \
    wget https://raw.githubusercontent.com/iltommi/mxe/master/src/hdf4-2-dllimport.patch; \
    patch -p1 -u < hdf4-1-portability-fixes.patch ; \
    patch -p1 -u < hdf4-2-dllimport.patch ; \
    libtoolize --force; \
    autoreconf --install; \
    mingw32-configure --disable-static --enable-shared  ac_cv_prog_HAVE_DOXYGEN="false" --disable-doxygen --disable-fortran --disable-netcdf LIBS="-lportablexdr -lws2_32"  CPPFLAGS="-DH4_F77_FUNC\(name,NAME\)=NAME -DH4_BUILT_AS_DYNAMIC_LIB=1 -DBIG_LONGS"; \
    make -C mfhdf/xdr -j $(nproc) LDFLAGS=-no-undefined; \
    make -C hdf/src -j $(nproc) LDFLAGS=-no-undefined; \
    make -C hdf/src -j 1 install; \
    make -C mfhdf/libsrc -j $(nproc) LDFLAGS="-no-undefined -ldf"; \
    make -C mfhdf/libsrc -j 1 install

# hdf5
# RUN wget https://support.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-1.8/hdf5-1.8.12/src/hdf5-1.8.12.tar.gz; \
#     tar -zxvf hdf5-1.8.12.tar.gz; \
#     cd hdf5-1.8.12; \
#     wget https://raw.githubusercontent.com/iltommi/mxe/master/src/hdf5-1-disable-configure-try-run.patch; \
#     wget https://raw.githubusercontent.com/iltommi/mxe/master/src/hdf5-2-platform-detection.patch; \
#     wget https://raw.githubusercontent.com/iltommi/mxe/master/src/hdf5-3-fix-autoconf-version.patch; \
#     patch -p1 -u < hdf5-1-disable-configure-try-run.patch; \
#     patch -p1 -u < hdf5-2-platform-detection.patch; \
#     patch -p1 -u < hdf5-3-fix-autoconf-version.patch; \
#     autoreconf --force --install; \
#     mingw32-configure --disable-static --enable-shared  ac_cv_prog_HAVE_DOXYGEN="false" --disable-doxygen --enable-cxx --disable-direct-vfd  CPPFLAGS='-DH5_HAVE_WIN32_API -DH5_HAVE_MINGW -DHAVE_WINDOWS_PATH -DH5_BUILT_AS_DYNAMIC_LIB'; \
#     sed -i 's,allow_undefined_flag="unsupported",allow_undefined_flag="",g' 'libtool'; \
#     for f in H5detect.exe H5make_libsettings.exe libhdf5.settings; do make -C src $f && install -m755 src/$f /usr/i686-w64-mingw32/sys-root/mingw/bin/; done; \
#     
        
# Neutrino
RUN git clone --recursive -j$(nproc) https://github.com/NeutrinoToolkit/Neutrino.git ; \
    cd Neutrino/PythonQt && mkdir cross && cd cross; \
    mingw32-cmake .. -DQt5_DIR=/usr/i686-w64-mingw32/sys-root/mingw/lib/cmake/Qt5 -DPythonQt_Wrap_QtAll=TRUE ;\
    make -j$(nproc) install; cd ../.. ; \
    mkdir cross && cd cross && mingw32-cmake .. && make -j$(nproc) package
 
 
#docker run --rm -v $(pwd):/mnt -t iltommi/neutrino-docker-cross /bin/sh -c 'cp /Neutrino/cross/Neutrino* /mnt'

