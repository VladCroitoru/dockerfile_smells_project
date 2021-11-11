# Java base image
FROM openjdk:8

# Tomcat 8.5

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# let "Tomcat Native" live somewhere isolated
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR

# runtime dependencies for Tomcat Native Libraries
# Tomcat Native 1.2+ requires a newer version of OpenSSL than debian:jessie has available
# > checking OpenSSL library version >= 1.0.2...
# > configure: error: Your version of OpenSSL is not compatible with this version of tcnative
# see http://tomcat.10.x6.nabble.com/VOTE-Release-Apache-Tomcat-8-0-32-tp5046007p5046024.html (and following discussion)
# and https://github.com/docker-library/tomcat/pull/31
ENV OPENSSL_VERSION 1.1.0f-3
RUN { \
        echo 'deb http://deb.debian.org/debian stretch main'; \
    } > /etc/apt/sources.list.d/stretch.list \
    && { \
# add a negative "Pin-Priority" so that we never ever get packages from stretch unless we explicitly request them
        echo 'Package: *'; \
        echo 'Pin: release n=stretch'; \
        echo 'Pin-Priority: -10'; \
        echo; \
# except OpenSSL, which is the reason we're here
        echo 'Package: openssl libssl*'; \
        echo "Pin: version $OPENSSL_VERSION"; \
        echo 'Pin-Priority: 990'; \
    } > /etc/apt/preferences.d/stretch-openssl
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        g++ \
        gcc \
        git \
        ipython \
        ipython-notebook \
        libapr1 \
        libatlas-dev \
        libatlas3gf-base \
        libavformat-dev \
        libblas3 \
        libfreetype6-dev \
        libjasper-dev \
        libjpeg-dev \
        liblapack-dev \
        liblapack3 \
        libpng-dev \
        libpq-dev \
        libswscale-dev \
        libtbb-dev \
        libtbb2 \
        libtiff-dev \
        make \
        openssl="$OPENSSL_VERSION" \
        pkg-config \
        python-dev \
        python-nose \
        python-pandas \
        python-sympy \
        python3 \
        python3-dev \
        python3-matplotlib \
        python3-numpy \
        python3-pip \
        python3-scipy \
        python3-setuptools \
        python3-tk \
        tcl \
        tk \
        unzip \
        wget \
        yasm \
    && rm -rf /var/lib/apt/lists/*

# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS
# see also "update.sh" (https://github.com/docker-library/tomcat/blob/master/update.sh)
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6 07E48665A34DCAFAE522E5E6266191C37C037D42 47309207D818FFD8DCD3F83F1931D684307A10A5 541FBE7D8F78B25E055DDEE13C370389288584E7 61B832AC2F1C5A90F0F9B00A1C506407564C17A3 713DA88BE50911535FE716F5208B0AB1D63011C7 79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED 9BA44C2621385CB966EBA586F72C284D731FABEE A27677289986DB50844682F8ACB77FC2E86E29AC A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23
RUN set -ex; \
    for key in $GPG_KEYS; do \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.5.15

# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
ENV TOMCAT_TGZ_URL https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
# not all the mirrors actually carry the .asc files :'(
ENV TOMCAT_ASC_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz.asc

RUN set -x \
    \
    && wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \
    && wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \
    && gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \
    && tar -xvf tomcat.tar.gz --strip-components=1 \
    && rm bin/*.bat \
    && rm tomcat.tar.gz* \
    \
    && nativeBuildDir="$(mktemp -d)" \
    && tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" --strip-components=1 \
    && nativeBuildDeps=" \
        dpkg-dev \
        gcc \
        libapr1-dev \
        libssl-dev \
        make \
        openjdk-${JAVA_VERSION%%[-~bu]*}-jdk=$JAVA_DEBIAN_VERSION \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $nativeBuildDeps && rm -rf /var/lib/apt/lists/* \
    && ( \
        export CATALINA_HOME="$PWD" \
        && cd "$nativeBuildDir/native" \
        && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
        && ./configure \
            --build="$gnuArch" \
            --libdir="$TOMCAT_NATIVE_LIBDIR" \
            --prefix="$CATALINA_HOME" \
            --with-apr="$(which apr-1-config)" \
            --with-java-home="$(docker-java-home)" \
            --with-ssl=yes \
        && make -j$(nproc) \
        && make install \
    ) \
# && apt-get purge -y --auto-remove $nativeBuildDeps \
    && rm -rf "$nativeBuildDir" \
    && rm bin/tomcat-native.tar.gz

# verify Tomcat Native is working properly
RUN set -e \
    && nativeLines="$(catalina.sh configtest 2>&1)" \
    && nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \
    && nativeLines="$(echo "$nativeLines" | sort -u)" \
    && if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat Native library' >&2; then \
        echo >&2 "$nativeLines"; \
        exit 1; \
    fi

EXPOSE 8080
CMD ["catalina.sh", "run"]

# Misc Python deps

RUN easy_install3 matplotlib

RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp34-cp34m-linux_x86_64.whl

RUN easy_install3 Pillow

# OpenCV and friends

RUN pip3 install numpy

WORKDIR /
RUN wget https://github.com/Itseez/opencv/archive/3.2.0.zip \
&& unzip 3.2.0.zip

    
RUN mkdir /opencv-3.2.0/cmake_binary \
&& cd /opencv-3.2.0/cmake_binary \
&& cmake -DBUILD_TIFF=ON \
  -DBUILD_opencv_java=OFF \
  -DWITH_CUDA=OFF \
  -DENABLE_AVX=OFF \
  -DENABLE_SSE3=OFF \
  -DENABLE_SSE4=OFF \
  -DWITH_OPENGL=ON \
  -DWITH_OPENCL=ON \
  -DWITH_IPP=ON \
  -DWITH_TBB=ON \
  -DWITH_EIGEN=ON \
  -DWITH_V4L=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=$(python3.4 -c "import sys; print(sys.prefix)") \
  -DPYTHON_EXECUTABLE=$(which python3.4) \
  -DPYTHON_INCLUDE_DIR=$(python3.4 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON_PACKAGES_PATH=$(python3.4 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \
&& make install \
&& rm /3.2.0.zip \
&& rm -r /opencv-3.2.0

RUN pip3 install flake8 pep8 --upgrade

RUN update-alternatives --set libblas.so.3 \
        /usr/lib/atlas-base/atlas/libblas.so.3 && \
    update-alternatives --set liblapack.so.3 \
        /usr/lib/atlas-base/atlas/liblapack.so.3

RUN pip3 install scikit-learn

# Numpy for tensorflow
RUN pip3 install --upgrade numpy
RUN easy_install3 numpy
