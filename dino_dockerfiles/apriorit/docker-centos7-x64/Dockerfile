FROM centos:7
MAINTAINER petrov <petrov@apriorit.com>

RUN yum -y update && yum clean all

#Install custom packages
RUN yum install -y epel-release

RUN yum groups mark convert
RUN yum groupinstall -y 'Development Tools'

RUN yum install -y clang clang-devel llvm-devel cmake3 cmake python-testtools python-pip wget
RUN yum install -y qt-creator protobuf-compiler graphviz libxml2-devel libxslt-devel
RUN yes | pip install checksumdir

#bzip2 need for bulding of boost iostream library
RUN yum -y install bzip2 bzip2-devel

#install newer subversion
RUN echo -e "[WandiscoSVN]\nname=Wandisco SVN Repo\nbaseurl=http://opensource.wandisco.com/centos/7/svn-1.8/RPMS/$basearch/\nenabled=1\ngpgcheck=0" > /etc/yum.repos.d/wandisco-svn.repo

RUN yum remove -y subversion*
RUN yum clean all
RUN yum install -y subversion

#install qt
RUN wget -q http://download.qt.io/archive/qt/5.7/5.7.1/qt-opensource-linux-x64-5.7.1.run

COPY resources /srv/resources
RUN chmod +x ./qt-opensource-linux-x64-5.7.1.run
RUN ./qt-opensource-linux-x64-5.7.1.run --script /srv/resources/qt-installer-noninteractive.qs -platform minimal

RUN ls /opt

RUN /opt/Qt5.7.1/Tools/QtCreator/bin/qbs setup-toolchains --detect 
RUN /opt/Qt5.7.1/Tools/QtCreator/bin/qbs setup-qt '/opt/Qt5.7.1/5.7/gcc_64/bin/qmake' QtProfile
RUN /opt/Qt5.7.1/Tools/QtCreator/bin/qbs config profiles.QtProfile.baseProfile clang
RUN yes | cp /opt/Qt5.7.1/5.7/gcc_64/lib/*.* /usr/lib64/

#building and installing of clang c++ library for better c++11 support
# http://stackoverflow.com/questions/25840088/how-to-build-libcxx-and-libcxxabi-by-clang-on-centos-7/25840107#25840107
# use "one command" style because of Docker copypaste convenience
#*******************************************
RUN libcxx="libcxx-3.8.1.src" && \
libcxxabi="libcxxabi-3.8.1.src" && \
tmp="tmpDirectory" && \
pwd && \
wget "http://llvm.org/releases/3.8.1/$libcxx.tar.xz" && \
tar xf "$libcxx.tar.xz" && \
cd $libcxx && \
pwd && \
mkdir $tmp && \
cd $tmp && \
pwd && \
ls -l && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ .. && \
make install && \
ln -s /usr/lib/libc++.so.1 /lib64 && \
cd .. && \
rm $tmp -rf && \
cd .. && \
wget "http://llvm.org/releases/3.8.1/$libcxxabi.tar.xz" && \
tar xf "$libcxxabi.tar.xz" && \
cd $libcxxabi && \
mkdir $tmp && \
cd $tmp && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DCMAKE_CXX_FLAGS="-std=c++11" -DLIBCXXABI_LIBCXX_INCLUDES=../../$libcxx/include .. && \
make install && \
ln -s /usr/lib/libc++abi.so.1 /lib64 && \
cd ../.. && \
cd $libcxx && \
mkdir $tmp && \
cd $tmp && \
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DLIBCXX_CXX_ABI=libcxxabi -DLIBCXX_CXX_ABI_INCLUDE_PATHS=../../$libcxxabi/include .. && \
make install && \
cd ../.. && \
rm -rf $libcxx $libcxxabi
#*******************************************
