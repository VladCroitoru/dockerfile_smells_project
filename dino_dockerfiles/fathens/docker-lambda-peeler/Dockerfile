FROM fathens/docker-lambda-opencv

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L http://www.netlib.org/lapack/lapack-3.6.0.tgz | tar -zxf - && cd lapack-* \
  && mkdir build && cd build \
  && cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=ON -D CMAKE_INSTALL_PREFIX=/var/task -D CMAKE_INSTALL_LIBDIR=lib ../ \
  && make install

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L http://users.ics.forth.gr/~lourakis/levmar/levmar-2.6.tgz | tar -zxf - && cd levmar-* \
  && mkdir build && cd build \
  && cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_DEMO=NO -D CMAKE_C_FLAGS=-fPIC ../ \
  && make \
  && ld -L/var/task/lib -llapack -shared -o /var/task/lib/liblevmar.so --whole-archive liblevmar.a \
  && cp -vu ../levmar.h /var/task/include/

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && yum update -y && yum install -y bzip2-devel \
  && curl -L http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.bz2 | tar -jxf - && cd boost_* \
  && ./bootstrap.sh --prefix=/var/task \
  && ./b2 install link=shared --without-python -j2 cxxflags="-std=c++11"

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L https://gmplib.org/download/gmp/gmp-6.1.1.tar.bz2 | tar -jxf - && cd gmp-* \
  && ./configure --prefix=/var/task \
  && make -j2 \
  && make check && make install

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L http://www.mpfr.org/mpfr-current/mpfr-3.1.4.tar.bz2 | tar -jxf - && cd mpfr-* \
  && curl http://www.mpfr.org/mpfr-3.1.4/allpatches | patch -N -Z -p1 \
  && ./configure --prefix=/var/task --with-gmp=/var/task \
  && make -j2 \
  && make check && make install

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L https://github.com/CGAL/cgal/releases/download/releases%2FCGAL-4.8.1/CGAL-4.8.1.zip | bsdtar -xf- && cd CGAL-* \
  && mkdir build && cd build \
  && cmake -D CMAKE_BUILD_TYPE=Release -D BUILD_SHARED_LIBS=ON -D CMAKE_INSTALL_PREFIX=/var/task -D WITH_BLAS=ON -D WITH_LAPACK=ON ../ \
  && make install

RUN set -x && cd /etc/yum.repos.d \
  && curl -sSLO https://s3.amazonaws.com/download.fpcomplete.com/centos/7/fpco.repo \
  && yum install -y stack

RUN set -x && mkdir -pv ~/tmp && cd ~/tmp \
  && curl -L http://nixos.org/releases/patchelf/patchelf-0.9/patchelf-0.9.tar.bz2 | tar -jxf - && cd patchelf-* \
  && ./configure \
  && make all && make install

RUN rm -rf ~/tmp \
  && echo "Build Complete: Version 1.3.0"
