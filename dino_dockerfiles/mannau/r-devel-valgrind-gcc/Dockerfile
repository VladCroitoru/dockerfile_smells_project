# Based on rocker/r-devel
## Emacs, make this -*- mode: sh; -*-

## start with the Docker 'base R' Debian-based image
FROM r-base:latest

## This handle reaches Carl and Dirk
MAINTAINER "Mario Annau" mario.annau@gmail.com

#ENV CC="clang-4.0 -fsanitize=address,undefined -fno-sanitize=float-divide-by-zero -fno-omit-frame-pointer"
#ENV CFLAGS=""
ENV HDF5_RELEASE_URL="https://support.hdfgroup.org/ftp/HDF5/releases"
ENV HDF5_VERSION=1.10.1
ENV LD_LIBRARY_PATH=/usr/local/lib

## Remain current
RUN apt-get update -qq \
	&& apt-get dist-upgrade -y

## From the Build-Depends of the Debian R package, plus subversion
RUN apt-get update -qq \
	&& apt-get install -t unstable -y --no-install-recommends \
		bash-completion \
		bison \
		debhelper \
		default-jdk \
		g++ \
		gcc \
		gdb \
		gfortran \
		groff-base \
		libblas-dev \
		libbz2-dev \
		libcairo2-dev/unstable \
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
		libxt-dev \
		mpack \
		subversion \
		tcl8.6-dev \
		texinfo \
		texlive-base \
		texlive-extra-utils \
		texlive-fonts-extra \
		texlive-fonts-recommended \
		texlive-generic-recommended \
		texlive-latex-base \
		texlive-latex-extra \
		texlive-latex-recommended \
		tk8.6-dev \
		x11proto-core-dev \
		xauth \
		xdg-utils \
		xfonts-base \
		xvfb \
		zlib1g-dev \
		valgrind \
		wget

# Install HDF5 release from source
RUN wget "$HDF5_RELEASE_URL/hdf5-${HDF5_VERSION%.*}/hdf5-$HDF5_VERSION/src/hdf5-$HDF5_VERSION.tar.gz" \
  && tar -xzf "hdf5-$HDF5_VERSION.tar.gz" \
  && cd "hdf5-$HDF5_VERSION" \
  && ./configure --prefix=/usr/local --enable-using-memchecker=yes --enable-memory-alloc-sanity-check=no --enable-build-mode=debug \
  && make install
  
## Check out R-devel
RUN cd /tmp \
&& svn co https://svn.r-project.org/R/trunk R-devel

## Build and install according the standard 'recipe' I emailed/posted years ago
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
		CFLAGS=$(R CMD config CFLAGS) \
		CXXFLAGS=$(R CMD config CXXFLAGS) \
	./configure --enable-R-shlib \
               --without-blas \
               --without-lapack \
               --with-readline \
               --without-recommended-packages \
               --program-suffix=dev \
               --with-valgrind-instrumentation=2 \
               --with-system-valgrind-headers \
               --enable-memory-profiling \
	&& make \
	&& make install \
	&& rm -rf /tmp/R-devel

## Set Renviron to get libs from base R install
RUN echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-library:/usr/local/lib/R/library:/usr/lib/R/library'}" >> /usr/local/lib/R/etc/Renviron

## Set default CRAN repo
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /usr/local/lib/R/etc/Rprofile.site

RUN cd /usr/local/bin \
&& mv R Rdevel \
&& mv Rscript Rscriptdevel \
&& ln -s Rdevel RD \
&& ln -s Rscriptdevel RDscript

# Install R dependencies
RUN Rdevel -e "install.packages(c('Rcpp', 'testthat', 'roxygen2', 'highlight', 'zoo', 'microbenchmark', 'knitr', 'rmarkdown', 'nycflights13', 'bit64'))"
