# This image creates a common scientific build environment that includes:
# gfortran, hdf4, hdf5, netcdf4

FROM gcc:latest

ENV BUILD /build
ENV OPT /opt

# last checked for updates Oct 18 2018
ENV ZLIB_VERSION 1.2.11
ENV JPEG_VERSION 6b
ENV SZIP_VERSION 2.1
ENV HDF4_VERSION 4.2.12
ENV HDF5_VERSION 1.10.4
ENV NC4F_VERSION 4.4.4
ENV NC4C_VERSION 4.4.1
ENV NCO_VERSION 4.6.1
ENV PYHDF_VERSION 0.9.0
ENV NETCDFPY_VERSION 1.2.4rel

# grab some packages we need
RUN apt-get update && apt-get install -y byacc bison diffutils flex make

# grab some convenience packages for using it as a build "machine"
RUN apt-get install -y vim less tree screen unzip cvs subversion git gdb valgrind

# this is our install dir for everything non-core
RUN mkdir -p ${OPT}

# add zlib
#RUN apt-get install -y zlib-devel
RUN mkdir -p ${BUILD} && cd ${BUILD} && \
    wget -q http://zlib.net/zlib-${ZLIB_VERSION}.tar.gz && \
    tar xzf zlib-${ZLIB_VERSION}.tar.gz && \
    cd zlib-${ZLIB_VERSION} && \
    ./configure && make -j4 && make install && \
    cp configure.log ${OPT}/config.log-zlib-${ZLIB_VERSION} && \
    rm -rf ${BUILD}

# add libjpeg
# NOTE: this has moved to: http://www.ijg.org/
# ... can we just use the one in debian instead?
#     https://packages.debian.org/search?keywords=libjpeg
RUN apt-get install -y libjpeg-dev
# RUN mkdir -p ${BUILD} && cd ${BUILD} && \
#     wget -q https://www.hdfgroup.org/ftp/lib-external/jpeg/src/jpegsrc.v${JPEG_VERSION}.tar.gz && \
#     tar xzf jpegsrc.v${JPEG_VERSION}.tar.gz && \
#     cd jpeg-${JPEG_VERSION} && \
#     ./configure && make -j4 && make install && \
#     cp config.log ${OPT}/config.log-jpeg-${JPEG_VERSION} && \
#     rm -rf ${BUILD}

## add szip
#RUN mkdir -p ${BUILD} && cd ${BUILD} && \
#    wget -q https://www.hdfgroup.org/ftp/lib-external/szip/${SZIP_VERSION}/src/szip-${SZIP_VERSION}.tar.gz && \
#    tar zxf szip-${SZIP_VERSION}.tar.gz && \
#    cd szip-${SZIP_VERSION} && \
#    ./configure --prefix="/usr" --with-pic && make -j4 && make install && \
#    cp config.log /opt/config.log-szip-${SZIP_VERSION} && \
#    rm -rf ${BUILD}

# add hdf4
RUN mkdir -p ${BUILD} ${OPT}/hdf4 && cd ${BUILD} && \
    wget -q http://www.hdfgroup.org/ftp/HDF/releases/HDF${HDF4_VERSION}/src/hdf-${HDF4_VERSION}.tar.gz && \
    tar xzf hdf-${HDF4_VERSION}.tar.gz && \
    cd hdf-${HDF4_VERSION} && \
    CFLAGS="-fPIC -DHAVE_NETCDF -fno-strict-aliasing" \
    CXXFLAGS="-fPIC -DHAVE_NETCDF -fno-strict-aliasing" \
    ./configure --prefix="${OPT}/hdf4" --disable-netcdf --enable-fortran && make -j4 && make install && \
    mv ${OPT}/hdf4/bin/ncdump ${OPT}/hdf4/bin/hdfdump && \
    mv ${OPT}/hdf4/bin/ncgen  ${OPT}/hdf4/bin/hdfgen && \
    cp config.log ${OPT}/hdf4/config.log-hdf4-${HDF4_VERSION} && \
    rm -rf ${BUILD}

# add hdf5
# note - hdf5 post-1.8.11 now includes -ldl as a dependency
# http://hdf-forum.184993.n3.nabble.com/Errors-compiling-against-Static-build-HDF5-1-8-11-Need-for-ldl-added-to-linker-arguments-td4026300.html

# looks like maybe we can work around it with a build flag?
# https://support.hdfgroup.org/ftp/HDF5/releases/ReleaseFiles/hdf5-1.10.0-patch1-RELEASE.txt
RUN mkdir -p ${BUILD} ${OPT}/hdf5 && cd ${BUILD} && \
    wget -q https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-${HDF5_VERSION}/src/hdf5-${HDF5_VERSION}.tar.bz2 && \
    tar xjf hdf5-${HDF5_VERSION}.tar.bz2 && \
    cd hdf5-${HDF5_VERSION} && \
    ./configure --prefix="${OPT}/hdf5" --with-pic --with-zlib="${OPT}/zlib" --enable-cxx --enable-fortran --enable-fortran2003 --with-pthread --with-default-api-version=v18 && make -j4 && make install && \
    cp config.log ${OPT}/hdf5/config.log-hdf5-${HDF5_VERSION} && \
    rm -rf ${BUILD}

# add netcdf-c
RUN mkdir -p ${BUILD} ${OPT}/netcdf4 && cd ${BUILD} && \
    wget -q ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-${NC4C_VERSION}.tar.gz && \
    tar xzf netcdf-${NC4C_VERSION}.tar.gz && \
    cd netcdf-${NC4C_VERSION} && \
    CPPFLAGS="-I${OPT}/hdf4/include -I${OPT}/hdf5/include" \
    LDFLAGS="-L${OPT}/hdf4/lib -L${OPT}/hdf5/lib" \
    LD_LIBRARY_PATH="${OPT}/zlib/lib:${OPT}/jpeg/lib:${OPT}/hdf4/lib:${OPT}/hdf5/lib" \
    LIBS="-ldf -lhdf5_hl -lhdf5 -ljpeg -lm -lz" \
    ./configure --prefix="${OPT}/netcdf4" --enable-hdf4 --disable-dap --with-pic  && make -j4 && make install && \
    cp config.log ${OPT}/netcdf4/config.log-netcdf-${NC4C_VERSION} && \
    rm -rf ${BUILD}

# add netcdf-fortran
# compiling against this requires -lnetcdff (note the extra f)
RUN mkdir -p ${BUILD} ${OPT}/netcdf4 && cd ${BUILD} && \
    wget -q ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-fortran-${NC4F_VERSION}.tar.gz && \
    tar xzf netcdf-fortran-${NC4F_VERSION}.tar.gz && \
    cd netcdf-fortran-${NC4F_VERSION} && \
    CPPFLAGS="-I${OPT}/hdf4/include -I${OPT}/hdf5/include -I${OPT}/netcdf4/include" \
    LDFLAGS="-L${OPT}/hdf4/lib -L${OPT}/hdf5/lib -L${OPT}/netcdf4/lib" \
    LD_LIBRARY_PATH="${OPT}/hdf4/lib:${OPT}/hdf5/lib:${OPT}/netcdf4/lib" \
    LIBS="-lnetcdf -ldf -lhdf5_hl -lhdf5 -ljpeg -lm -lz" \
    ./configure --prefix="${OPT}/netcdf4" --disable-dap --with-pic && make -j4 && make install && \
    cp config.log ${OPT}/netcdf4/config.log-netcdff-${NC4F_VERSION} && \
    rm -rf ${BUILD}

# add the nco utilities for basic netcdf manipulation
RUN mkdir -p ${BUILD} ${OPT}/nco && cd ${BUILD} && \
    wget -qL https://github.com/nco/nco/archive/${NCO_VERSION}.tar.gz && \
    tar xzf ${NCO_VERSION}.tar.gz && \
    cd nco-${NCO_VERSION} && \
    NETCDF_ROOT=${OPT}/netcdf4 ./configure --prefix=${OPT}/nco && \
    make && make install && \
    rm -rf ${BUILD}

## add uwglance for verifying data, etc.
RUN apt-get install -y python-setuptools python-numpy python-scipy python-matplotlib python-mpltoolkits.basemap
RUN easy_install -f http://larch.ssec.wisc.edu/cgi-bin/repos.cgi uwglance

# ## add pyhdf for glance to read hdf4 files
# RUN mkdir -p ${BUILD} && cd ${BUILD} && \
#     wget -q http://hdfeos.org/software/pyhdf/pyhdf-${PYHDF_VERSION}.tar.gz && \
#     tar xzf pyhdf-${PYHDF_VERSION}.tar.gz && \
#     cd pyhdf-${PYHDF_VERSION} && \
#     INCLUDE_DIRS="${OPT}/hdf4/include/" \
#     LIBRARY_DIRS="${OPT}/hdf4/lib/" \
#     python setup.py install && \
#     rm -r ${BUILD}

## add netcdf4-python for glance to read netcdf4 files
RUN mkdir -p ${BUILD} && cd ${BUILD} && \
    wget -q https://github.com/Unidata/netcdf4-python/archive/v${NETCDFPY_VERSION}.tar.gz && \
    tar xzf v${NETCDFPY_VERSION}.tar.gz && \
    cd netcdf4-python-${NETCDFPY_VERSION} && \
    PATH="${OPT}/netcdf4/bin:$PATH" \
    python setup.py install && \
    rm -r ${BUILD}

# throw in some shell niceties
RUN echo 'alias ls="ls --color=auto"' >> ~/.bashrc && \
    echo 'alias ll="ls -lGh $@"' >> ~/.bashrc

# set these so future shells pick them up too
ENV HDF4 ${OPT}/hdf4
ENV HDF5 ${OPT}/hdf5
ENV NETCDF ${OPT}/netcdf4
ENV LD_LIBRARY_PATH ${HDF4}/lib:${HDF5}/lib:${NETCDF}/lib:${LD_LIBRARY_PATH}

ENV PATH ${HDF4}/bin/:${HDF5}/bin:${NETCDF}/bin:${PATH}
