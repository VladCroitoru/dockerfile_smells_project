## Emacs, make this -*- mode: sh; -*-

## Modification of the Dockerfile originally created by Dirk
## Eddelbuettel and Carl Boettiger at https://github.com/rocker-org/rocker

## start with the Docker 'base R' Debian-based image
FROM r-base:latest

MAINTAINER "Francois Michonneau" francois.michonneau@gmail.com

## Remain current
RUN apt-get update -qq \
	&& apt-get dist-upgrade -y

## From the Build-Depends of the Debian R package, plus subversion, and gcc-5.1/g++-5.1
##
## Also add   git autotools-dev automake  so that we can build littler from source
##
RUN apt-get update -qq \
	&& apt-get install -t unstable -y --no-install-recommends \
		automake \
		autotools-dev \
		bash-completion \
		bison \
		clang-3.5 \
		debhelper \
		default-jdk \
		g++ \
		g++-5 \
		gcc-5 \
		gcc \
		gfortran \
		gfortran-5 \
		git \
		groff-base \
		libblas-dev \
		libbz2-dev \
		libcairo2-dev \
		libcurl4-openssl-dev \
		libjpeg-dev \
		liblapack-dev \
		liblzma-dev \
		libncurses5-dev \
		libpango1.0-dev \
		libpcre3-dev \
		libpng-dev \
		libreadline-dev \
		libtiff5-dev \
		libx11-dev \
		libxml2-dev \
		libxslt1-dev \
		libxt-dev \
		mpack \
		rsync \
		subversion \
		tcl8.5-dev \
		texinfo \
		texlive-base \
		texlive-extra-utils \
		texlive-fonts-extra \
		texlive-fonts-recommended \
		texlive-generic-recommended \
		texlive-latex-base \
		texlive-latex-extra \
		texlive-latex-recommended \
		tk8.5-dev \
		valgrind \
		x11proto-core-dev \
		xauth \
		xdg-utils \
		xfonts-base \
		xvfb \
		zlib1g-dev

## Check out R-devel
RUN cd /tmp \
    && svn co http://svn.r-project.org/R/trunk R-devel

## Download the sources for the recommended packages
RUN cd /tmp/R-devel \
    && ./tools/rsync-recommended

## Build and install according extending the standard 'recipe' I emailed/posted years ago
## Modified to use the same flags as listed here: http://www.stats.ox.ac.uk/pub/bdr/memtests/README.txt
RUN cd /tmp/R-devel \
	&& R_PAPERSIZE=letter \
	   R_BATCHSAVE="--no-save --no-restore" \
	   R_BROWSER=xdg-open \
	   PAGER=/usr/bin/pager \
	   PERL=/usr/bin/perl \
	   R_UNZIPCMD=/usr/bin/unzip \
	   R_ZIPCMD=/usr/bin/zip \
	   R_PRINTCMD=/usr/bin/lpr \
	   LIBnn=lib \
	   AWK=/usr/bin/awk \
	   CFLAGS="-g -O2 -Wall -pedantic -mtune=native -fsanitize=address" \
	   CXXFLAGS="-g -O2 -Wall -pedantic -mtune=native" \
	   MAIN_LDFLAGS="-fsanitize=address,undefined" \
	   FFLAGS="-g -O2 -mtune=native" \
	   FCFLAGS="-g -O2 -mtune=native" \
	   CC="gcc-5 -std=gnu99 -fsanitize=address,undefined -fno-omit-frame-pointer" \
	   CXX="g++-5 -std=c++11 -fsanitize=address,undefined -fno-omit-frame-pointer" \
	   CXX1X="g++-5 -std=c++11 -fsanitize=address,undefined -fno-omit-frame-pointer" \
	   FC="gfortran-5 -fsanitize=address" \
	   F77="gfortran-5 -fsanitize=address" \
	   ./configure --enable-R-shlib \
	       --without-blas \
	       --without-lapack \
	       --with-readline \
	       --program-suffix=dev \
	       --disable-openmp \
	&& make \
	&& make install \
	&& make clean

## Set Renviron to get libs from base R install
RUN echo "R_LIBS=\${R_LIBS-'/R-dev/R-docker-libs:/usr/local/lib/R/site-library:/usr/local/lib/R/library:/usr/lib/R/library'}" >> /usr/local/lib/R/etc/Renviron

## Set default CRAN repo
RUN echo 'options("repos"="http://cran.rstudio.com")' >> /usr/local/lib/R/etc/Rprofile.site

## Create Makevars file similar to http://www.stats.ox.ac.uk/pub/bdr/memtests/README.txt
RUN mkdir $HOME/.R/ \
    && echo "CC = gcc-5 -std=gnu99 -fsanitize=address,undefined -fno-omit-frame-pointer" >> $HOME/.R/Makevars \
    && echo "CXX = g++-5 -std=c++11 -fsanitize=address,undefined -fno-omit-frame-pointer" >> $HOME/.R/Makevars \
    && echo "CXX1X = g++-5 -std=c++11 -fsanitize=address,undefined -fno-omit-frame-pointer" >> $HOME/.R/Makevars \
    && echo "F77 = gfortran-5 -fsanitize=address" >> $HOME/.R/Makevars \
    && echo "FC = gfortran-5 -fsanitize=address" >> $HOME/.R/Makevars \
    && echo "FCFLAGS = -g -O2 -mtune=native -fbounds-check" >> $HOME/.R/Makevars \
    && echo "FFLAGS = -g -O2 -mtune=native -fbounds-check" >> $HOME/.R/Makevars \
    && echo "CFLAGS = -I/usr/include/libxml2" >> $HOME/.R/Makevars

RUN export ASAN_OPTIONS='detect_leaks=0:detect_odr_violation=0'


## to also build littler against RD
##   1)	 apt-get install git autotools-dev automake
##   2)	 use CC from RD CMD config CC, ie same as R
##   3)	 use PATH to include RD's bin, ie
## ie
##   CC="clang-3.5 -fsanitize=undefined -fno-sanitize=float-divide-by-zero,vptr,function -fno-sanitize-recover" \
##   PATH="/usr/local/lib/R/bin/:$PATH" \
##   ./bootstrap

## Check out littler
#RUN cd /tmp \
#	&& git clone https://github.com/eddelbuettel/littler.git

# RUN cd /tmp/littler \
# 	&& CC="clang-3.5 -fsanitize=undefined -fno-sanitize=float-divide-by-zero,vptr,function -fno-sanitize-recover" PATH="/usr/local/lib/R/bin/:$PATH" ./bootstrap \
# 	&& ./configure --prefix=/usr \
# 	&& make \
# 	&& make install \
# 	&& cp -vax examples/*.r /usr/local/bin

RUN cd /usr/local/bin \
	&& mv R Rdevel \
	&& mv Rscript Rscriptdevel \
	&& ln -s Rdevel RD \
	&& ln -s Rscriptdevel RDscript
