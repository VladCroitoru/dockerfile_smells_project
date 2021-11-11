# we use metwork/centos6 because of centos6 EOL
FROM metwork/centos6:latest

RUN yum -y install createrepo wget bzip2 patch make automake file gcc gcc-c++ gcc-gfortran antlr libtool texinfo bison flex perl-XML-Parser swig gettext libjpeg-turbo freetype fontconfig jasper-libs python-devel zlib-devel bzip2-devel libjpeg-turbo-devel freetype-devel fontconfig-devel jasper-devel rpm-build xz expat-devel bc which git nspr-devel nss-devel file-devel popt-devel elfutils-devel elfutils elfutils-libelf-devel elfutils-libelf elfutils-libs openblas-devel valgrind ncurses-devel gperf devtoolset-8 rh-python35 libX11-devel libXft-devel libXrender-devel libXext-devel pixman-devel libuuid-devel && rpm -qa |sort |md5sum |awk '{print $1;}' >/etc/buildimage_hash
