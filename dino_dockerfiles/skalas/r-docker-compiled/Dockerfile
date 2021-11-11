FROM ubuntu:14.04
MAINTAINER Miguel Escalante <miguel@opi.la>

RUN apt-get update \
&& apt-get install -y build-essential \
libpq-dev \
liblapack3 \
libblas3 \
libmysql++-dev \
sqlite3 \
fort77 \
gnuplot-x11 \
gfortran \
texinfo \
liblapack-dev \
liblapack3gf \
texi2html \
libglpk-dev \
libgeos-dev \
libgdal1-dev \
libproj-dev \
wget \
git \
curl\
&& apt-get build-dep -y r-base \
&& wget --no-verbose http://cran.r-project.org/src/base/R-latest.tar.gz -O /tmp/R-latest.tar.gz \
&& tar -xzvf /tmp/R-latest.tar.gz -C /tmp/ \
&& cd $(ls -dt /tmp/R-*/ | head -1 ) \
&& ./configure \
--enable-memory-profiling \
--enable-R-shlib \
--with-blas \
--with-lapack \
--with-system-zlib \
--with-system-bzlib \
--with-system-xz \
--with-tcltk  \
--with-cairo \
--with-libpng \
--with-jpeglib \
--with-libtiff \
&& make \
&& make install \
&& rm -rf /tmp/*
CMD ["R"]
