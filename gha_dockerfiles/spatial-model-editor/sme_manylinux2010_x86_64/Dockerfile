# manylinux2010-based image for compiling Spatial Model Editor python wheels

FROM quay.io/pypa/manylinux2010_x86_64:2021-10-11-14ac00e as builder

ARG NPROCS=24
ARG BUILD_DIR=/opt/smelibs
ARG TMP_DIR=/opt/tmpwd

RUN /opt/python/cp39-cp39/bin/pip install ninja \
    && ln -fs /opt/python/cp39-cp39/bin/ninja /usr/bin/ninja

ARG CEREAL_VERSION="master"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $CEREAL_VERSION \
        --depth=1 \
        https://github.com/USCiLab/cereal.git \
    && cd cereal \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DJUST_INSTALL_CEREAL=ON \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        .. \
    && ninja install \
    && rm -rf $TMP_DIR

ARG GMP_VERSION="6.2.1"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && curl \
        https://gmplib.org/download/gmp/gmp-${GMP_VERSION}.tar.bz2 \
        --output gmp.tar.bz2 \
    && tar xjf gmp.tar.bz2 \
    && cd gmp-${GMP_VERSION} \
    && ./configure \
        --prefix=$BUILD_DIR \
        --disable-shared \
        --host=x86_64-unknown-linux-gnu \
        --enable-static \
        --with-pic \
        --enable-cxx \
    && make -j$NPROCS \
    && make check \
    && make install \
    && rm -rf $TMP_DIR

ARG MPFR_VERSION="4.1.0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && curl \
        https://www.mpfr.org/mpfr-current/mpfr-${MPFR_VERSION}.tar.bz2 \
        --output mpfr.tar.bz2 \
    && tar xjf mpfr.tar.bz2 \
    && cd mpfr-${MPFR_VERSION} \
    && ./configure \
        --prefix=$BUILD_DIR \
        --disable-shared \
        --host=x86_64-unknown-linux-gnu \
        --enable-static \
        --with-pic \
        --with-gmp-lib=$BUILD_DIR/lib \
        --with-gmp-include=$BUILD_DIR/include \
    && make -j$NPROCS \
    && make check \
    && make install \
    && rm -rf $TMP_DIR

ARG BOOST_VERSION="1.77.0"
ARG BOOST_VERSION_="1_77_0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && curl -L \
        "https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.bz2" \
        --output boost.tar.bz2 \
    && tar xjf boost.tar.bz2 \
    && cd boost_${BOOST_VERSION_} \
    && cp -r boost $BUILD_DIR/include/. \
    && rm -rf $TMP_DIR

ARG CGAL_VERSION="v5.3"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $CGAL_VERSION \
        --depth=1 \
        https://github.com/CGAL/cgal.git \
    && cd cgal \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        .. \
    && ninja \
    && ninja install \
    && rm -rf $TMP_DIR

ARG LIBEXPAT_VERSION="R_2_4_1"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $LIBEXPAT_VERSION \
        --depth=1 \
        https://github.com/libexpat/libexpat.git \
    && cd libexpat \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DEXPAT_BUILD_DOCS=OFF \
        -DEXPAT_BUILD_EXAMPLES=OFF \
        -DEXPAT_BUILD_TOOLS=OFF \
        -DEXPAT_SHARED_LIBS=OFF \
        ../expat \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG LIBTIFF_VERSION="v4.3.0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $LIBTIFF_VERSION \
        --depth=1 \
        https://gitlab.com/libtiff/libtiff.git \
    && cd libtiff \
    && mkdir cmake-build \
    && cd cmake-build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -Djpeg=OFF \
        -Djpeg12=OFF \
        -Djbig=OFF \
        -Dlzma=OFF \
        -Dlibdeflate=OFF \
        -Dpixarlog=OFF \
        -Dold-jpeg=OFF \
        -Dzstd=OFF \
        -Dmdi=OFF \
        -Dwebp=OFF \
        -Dzlib=OFF \
        -DGLUT_INCLUDE_DIR=GLUT_INCLUDE_DIR-NOTFOUND \
        -DOPENGL_INCLUDE_DIR=OPENGL_INCLUDE_DIR-NOTFOUND \
        .. \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG LLVM_VERSION="13.0.0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b llvmorg-$LLVM_VERSION \
        --depth=1 \
        https://github.com/llvm/llvm-project.git \
    && cd llvm-project/llvm \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DPython3_EXECUTABLE:FILEPATH=/opt/python/cp39-cp39/bin/python \
        -DLLVM_DEFAULT_TARGET_TRIPLE=x86_64-unknown-linux-gnu \
        -DLLVM_TARGETS_TO_BUILD="X86" \
        -DLLVM_BUILD_TOOLS=OFF \
        -DLLVM_INCLUDE_TOOLS=OFF \
        -DLLVM_BUILD_EXAMPLES=OFF \
        -DLLVM_INCLUDE_EXAMPLES=OFF \
        -DLLVM_BUILD_TESTS=OFF \
        -DLLVM_INCLUDE_TESTS=OFF \
        -DLLVM_INCLUDE_DOCS=OFF \
        -DLLVM_BUILD_UTILS=OFF \
        -DLLVM_INCLUDE_UTILS=OFF \
        -DLLVM_INCLUDE_GO_TESTS=OFF \
        -DLLVM_BUILD_BENCHMARKS=OFF \
        -DLLVM_INCLUDE_BENCHMARKS=OFF \
        -DLLVM_ENABLE_LIBPFM=OFF \
        -DLLVM_ENABLE_ZLIB=OFF \
        -DLLVM_ENABLE_DIA_SDK=OFF \
        -DLLVM_BUILD_INSTRUMENTED_COVERAGE=OFF \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DLLVM_ENABLE_RTTI=ON \
        -DLLVM_ENABLE_TERMINFO=OFF \
        -DLLVM_ENABLE_LIBXML2=OFF \
        -DLLVM_ENABLE_WARNINGS=OFF \
        .. \
    && ninja \
    && ninja install \
    && rm -rf $TMP_DIR

ARG TBB_VERSION="v2020.3"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $TBB_VERSION \
        --depth=1 \
        https://github.com/intel/tbb.git \
    && cd tbb \
    && make tbb \
        stdver=c++17 \
        extra_inc=big_iron.inc \
        -j$NPROCS \
    && mkdir -p $BUILD_DIR/lib \
    && cp build/*_release/*.a $BUILD_DIR/lib \
    && mkdir -p $BUILD_DIR/include \
    && cp -r include/tbb $BUILD_DIR/include/. \
    && rm -rf $TMP_DIR

ARG MUPARSER_VERSION="v2.3.2"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $MUPARSER_VERSION \
        --depth=1 \
        https://github.com/beltoforion/muparser.git \
    && cd muparser \
    && mkdir cmake-build \
    && cd cmake-build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DBUILD_TESTING=ON \
        -DENABLE_OPENMP=OFF \
        -DENABLE_SAMPLES=OFF \
        .. \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG QT_VERSION="v6.2.0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        https://code.qt.io/qt/qt5.git \
    && cd qt5 \
    && git checkout $QT_VERSION \
    && git submodule update --init qtbase \
    && cd .. \
    && mkdir build \
    && cd build \
    && cmake ../qt5/qtbase \
        -GNinja \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=${BUILD_DIR} \
        -DFEATURE_system_doubleconversion=OFF \
        -DFEATURE_system_harfbuzz=OFF \
        -DFEATURE_system_jpeg=OFF \
        -DFEATURE_system_libb2=OFF \
        -DFEATURE_system_pcre2=OFF \
        -DFEATURE_system_png=OFF \
        -DFEATURE_system_proxies=OFF \
        -DFEATURE_system_textmarkdownreader=OFF \
        -DFEATURE_system_zlib=OFF \
        -DFEATURE_zstd=OFF \
        -DFEATURE_openssl=OFF \
        -DFEATURE_sql=OFF \
        -DFEATURE_icu=OFF \
        -DFEATURE_testlib=ON \
        -DBUILD_WITH_PCH=OFF \
        -DFEATURE_xcb=OFF \
    && ninja \
    && ninja install \
    && rm -rf $TMP_DIR

ARG ZLIB_VERSION="v1.2.11"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $ZLIB_VERSION \
        --depth=1 \
        https://github.com/madler/zlib.git \
    && cd zlib \
    && mkdir build \
    && cd build \
    && cmake .. \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
    && ninja zlibstatic \
    && cp libz.a $BUILD_DIR/lib/libz.a \
    && cp zconf.h $BUILD_DIR/include/. \
    && cp ../zlib.h $BUILD_DIR/include/. \
    && rm -rf $TMP_DIR

ARG OPENCV_VERSION="4.5.4"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $OPENCV_VERSION \
        --depth=1 \
        https://github.com/opencv/opencv.git \
    && cd opencv \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DBUILD_opencv_apps=OFF \
        -DBUILD_opencv_calib3d=OFF \
        -DBUILD_opencv_core=ON \
        -DBUILD_opencv_dnn=OFF \
        -DBUILD_opencv_features2d=OFF \
        -DBUILD_opencv_flann=OFF \
        -DBUILD_opencv_gapi=OFF \
        -DBUILD_opencv_highgui=OFF \
        -DBUILD_opencv_imgcodecs=OFF \
        -DBUILD_opencv_imgproc=ON \
        -DBUILD_opencv_java_bindings_generator=OFF \
        -DBUILD_opencv_js=OFF \
        -DBUILD_opencv_ml=OFF \
        -DBUILD_opencv_objdetect=OFF \
        -DBUILD_opencv_photo=OFF \
        -DBUILD_opencv_python_bindings_generator=OFF \
        -DBUILD_opencv_python_tests=OFF \
        -DBUILD_opencv_stitching=OFF \
        -DBUILD_opencv_ts=OFF \
        -DBUILD_opencv_video=OFF \
        -DBUILD_opencv_videoio=OFF \
        -DBUILD_opencv_world=OFF \
        -DBUILD_CUDA_STUBS:BOOL=OFF \
        -DBUILD_DOCS:BOOL=OFF \
        -DBUILD_EXAMPLES:BOOL=OFF \
        -DBUILD_FAT_JAVA_LIB:BOOL=OFF \
        -DBUILD_IPP_IW:BOOL=OFF \
        -DBUILD_ITT:BOOL=OFF \
        -DBUILD_JASPER:BOOL=OFF \
        -DBUILD_JAVA:BOOL=OFF \
        -DBUILD_JPEG:BOOL=OFF \
        -DBUILD_OPENEXR:BOOL=OFF \
        -DBUILD_PACKAGE:BOOL=OFF \
        -DBUILD_PERF_TESTS:BOOL=OFF \
        -DBUILD_PNG:BOOL=OFF \
        -DBUILD_PROTOBUF:BOOL=OFF \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DBUILD_TBB:BOOL=OFF \
        -DBUILD_TESTS:BOOL=OFF \
        -DBUILD_TIFF:BOOL=OFF \
        -DBUILD_USE_SYMLINKS:BOOL=OFF \
        -DBUILD_WEBP:BOOL=OFF \
        -DBUILD_WITH_DEBUG_INFO:BOOL=OFF \
        -DBUILD_WITH_DYNAMIC_IPP:BOOL=OFF \
        -DBUILD_ZLIB:BOOL=OFF \
        -DWITH_1394:BOOL=OFF \
        -DWITH_ADE:BOOL=OFF \
        -DWITH_ARAVIS:BOOL=OFF \
        -DWITH_CLP:BOOL=OFF \
        -DWITH_CUDA:BOOL=OFF \
        -DWITH_EIGEN:BOOL=OFF \
        -DWITH_FFMPEG:BOOL=OFF \
        -DWITH_FREETYPE:BOOL=OFF \
        -DWITH_GDAL:BOOL=OFF \
        -DWITH_GDCM:BOOL=OFF \
        -DWITH_GPHOTO2:BOOL=OFF \
        -DWITH_GSTREAMER:BOOL=OFF \
        -DWITH_GTK:BOOL=OFF \
        -DWITH_GTK_2_X:BOOL=OFF \
        -DWITH_HALIDE:BOOL=OFF \
        -DWITH_HPX:BOOL=OFF \
        -DWITH_IMGCODEC_HDR:BOOL=OFF \
        -DWITH_IMGCODEC_PFM:BOOL=OFF \
        -DWITH_IMGCODEC_PXM:BOOL=OFF \
        -DWITH_IMGCODEC_SUNRASTER:BOOL=OFF \
        -DWITH_INF_ENGINE:BOOL=OFF \
        -DWITH_IPP:BOOL=OFF \
        -DWITH_ITT:BOOL=OFF \
        -DWITH_JASPER:BOOL=OFF \
        -DWITH_JPEG:BOOL=OFF \
        -DWITH_LAPACK:BOOL=OFF \
        -DWITH_LIBREALSENSE:BOOL=OFF \
        -DWITH_MFX:BOOL=OFF \
        -DWITH_NGRAPH:BOOL=OFF \
        -DWITH_OPENCL:BOOL=OFF \
        -DWITH_OPENCLAMDBLAS:BOOL=OFF \
        -DWITH_OPENCLAMDFFT:BOOL=OFF \
        -DWITH_OPENCL_SVM:BOOL=OFF \
        -DWITH_OPENEXR:BOOL=OFF \
        -DWITH_OPENGL:BOOL=OFF \
        -DWITH_OPENJPEG:BOOL=OFF \
        -DWITH_OPENMP:BOOL=OFF \
        -DWITH_OPENNI:BOOL=OFF \
        -DWITH_OPENNI2:BOOL=OFF \
        -DWITH_OPENVX:BOOL=OFF \
        -DWITH_PLAIDML:BOOL=OFF \
        -DWITH_PNG:BOOL=OFF \
        -DWITH_PROTOBUF:BOOL=OFF \
        -DWITH_PTHREADS_PF:BOOL=OFF \
        -DWITH_PVAPI:BOOL=OFF \
        -DWITH_QT:BOOL=OFF \
        -DWITH_QUIRC:BOOL=OFF \
        -DWITH_TBB:BOOL=OFF \
        -DWITH_TIFF:BOOL=OFF \
        -DWITH_V4L:BOOL=OFF \
        -DWITH_VA:BOOL=OFF \
        -DWITH_VA_INTEL:BOOL=OFF \
        -DWITH_VTK:BOOL=OFF \
        -DWITH_VULKAN:BOOL=OFF \
        -DWITH_WEBP:BOOL=OFF \
        -DWITH_XIMEA:BOOL=OFF \
        -DWITH_XINE:BOOL=OFF \
        -DZLIB_INCLUDE_DIR=$BUILD_DIR/include \
        -DZLIB_LIBRARY_RELEASE=$BUILD_DIR/lib/libz.a \
        .. \
    && ninja \
    && ninja install \
    && rm -rf $TMP_DIR

ARG FMT_VERSION="8.0.1"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $FMT_VERSION \
        --depth=1 \
        https://github.com/fmtlib/fmt.git \
    && cd fmt \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DCMAKE_CXX_STANDARD=17 \
        -DFMT_DOC=OFF \
        .. \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG SPDLOG_VERSION="v1.9.2"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $SPDLOG_VERSION \
        --depth=1 \
        https://github.com/gabime/spdlog.git \
    && cd spdlog \
    && mkdir cmake-build \
    && cd cmake-build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DSPDLOG_BUILD_TESTS=ON \
        -DSPDLOG_BUILD_EXAMPLE=OFF \
        -DSPDLOG_FMT_EXTERNAL=ON \
        -DSPDLOG_NO_THREAD_ID=ON \
        -DSPDLOG_NO_ATOMIC_LEVELS=ON \
        -DCMAKE_PREFIX_PATH=$BUILD_DIR \
        .. \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG SYMENGINE_VERSION="master"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $SYMENGINE_VERSION \
        --depth=1 \
        https://github.com/symengine/symengine.git \
    && cd symengine \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DBUILD_BENCHMARKS=OFF \
        -DGMP_INCLUDE_DIR=$BUILD_DIR/include \
        -DGMP_LIBRARY=$BUILD_DIR/lib/libgmp.a \
        -DCMAKE_PREFIX_PATH=$BUILD_DIR \
        -DWITH_LLVM=ON \
        -DWITH_COTIRE=OFF \
        -DWITH_SYMENGINE_THREAD_SAFE=OFF \
        .. \
    && ninja \
    && ninja test \
    && ninja install \
    && rm -rf $TMP_DIR

ARG DUNE_COPASI_VERSION="releases/1.1"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && export DUNE_COPASI_USE_STATIC_DEPS=ON \
    && export CMAKE_INSTALL_PREFIX=$BUILD_DIR \
    && export MAKE_FLAGS="-j$NPROCS VERBOSE=1" \
    && export DUNE_USE_FALLBACK_FILESYSTEM=ON \
    && export CMAKE_CXX_FLAGS="-fvisibility=hidden" \
    && export CMAKE_FLAGS="-GNinja" \
    && git clone \
        -b $DUNE_COPASI_VERSION \
        --depth 1 \
        https://gitlab.dune-project.org/copasi/dune-copasi.git \
    && cd dune-copasi \
    && bash dune-copasi.opts \
    && bash .ci/setup_dune "$PWD"/dune-copasi.opts \
    && bash .ci/install "$PWD"/dune-copasi.opts \
    && rm -rf $TMP_DIR

ARG LIBSBML_VERSION="v5.19.0"
RUN mkdir -p $TMP_DIR && cd $TMP_DIR \
    && git clone \
        -b $LIBSBML_VERSION \
        --depth=1 \
        https://github.com/sbmlteam/libsbml.git \
    && cd libsbml \
    && mkdir build \
    && cd build \
    && cmake \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=OFF \
        -DCMAKE_C_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_CXX_FLAGS="-fpic -fvisibility=hidden" \
        -DCMAKE_INSTALL_PREFIX=$BUILD_DIR \
        -DENABLE_SPATIAL=ON \
        -DWITH_CPP_NAMESPACE=ON \
        -DLIBSBML_SKIP_SHARED_LIBRARY=ON \
        -DWITH_BZIP2=OFF \
        -DWITH_ZLIB=ON \
        -DLIBZ_INCLUDE_DIR=$BUILD_DIR/include \
        -DLIBZ_LIBRARY=$BUILD_DIR/lib/libz.a \
        -DWITH_SWIG=OFF \
        -DWITH_LIBXML=OFF \
        -DWITH_EXPAT=ON \
        -DLIBEXPAT_INCLUDE_DIR=$BUILD_DIR/include \
        -DLIBEXPAT_LIBRARY=$BUILD_DIR/lib64/libexpat.a \
        .. \
    && ninja \
    && ninja install \
    && rm -rf $TMP_DIR

FROM quay.io/pypa/manylinux2010_x86_64:2021-10-11-14ac00e

ARG BUILD_DIR=/opt/smelibs

# Install ccache
RUN yum install -q -y \
        ccache-3.1.6 \
    && yum clean all

# Setup ccache
ENV CCACHE_DIR=/tmp/ccache
ENV CCACHE_BASEDIR=/tmp
ENV CMAKE_CXX_COMPILER_LAUNCHER="ccache"

# SME static libs
COPY --from=builder $BUILD_DIR $BUILD_DIR
ENV CMAKE_PREFIX_PATH="$BUILD_DIR;$BUILD_DIR/lib64/cmake"
