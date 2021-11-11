FROM centos:7

MAINTAINER Philipp von Bieberstein, Asher Baltzell

ENTRYPOINT ["/bin/bash"]

RUN yum group install "Development Tools" -y \
	&& yum install vim -y\
	&& yum install wget -y \
	&& yum install gsl -y \
	&& yum install boost -y \
	&& yum install lapack -y \
	&& yum install gsl-devel -y \
	&& yum -y install python-devel \
	&& yum -y install mlocate \
	&& yum -y install boost-devel \
	&& yum -y install fftw \
	&& yum -y install fftw-devel \
	&& yum -y install zlib \
	&& yum -y install zlib-devel

RUN mkdir ~/repos \
	&& cd ~/repos \
	&& wget http://www.iplantcollaborative.org/sites/default/files/irods/icommands.x86_64.tar.bz2 \
	&& tar xfvj icommands.x86_64.tar.bz2

RUN mkdir ~/library/bin -p \
	&& mkdir ~/library/include -p \
	&& mkdir ~/library/lib -p

ENV PATH /root/library/bin:$PATH
ENV PATH /root/repos/icommands:$PATH
ENV LD_LIBRARY_PATH /root/library/lib:$LD_LIBRARY_PATH
ENV INCLUDE /root/library/lib:$INCLUDE
ENV PYTHONPATH /root/library/lib/python2.7/site-packages/

RUN cd ~/repos \
	&& wget ftp://heasarc.gsfc.nasa.gov/software/fitsio/c/cfitsio_latest.tar.gz \
	&& tar xfvz cfitsio_latest.tar.gz \
	&& cd cfitsio \
	&& ./configure --prefix=/root/library \
	&& make \
	&& make install

RUN cd ~/repos \
	&& wget http://www.iausofa.org/2015_0209_C/sofa_c-20150209_a.tar.gz \
	&& tar xfvz sofa_c-20150209_a.tar.gz \
	&& cd sofa/20150209_a/c/src \
	&& echo extraction done - now editing makefile \
	&& sed -i 's#INSTALL_DIR = $(HOME)#INSTALL_DIR = $(HOME)/library#' makefile \
	&& sed -i 's#CFLAGF = -c -pedantic -Wall -W -O#CFLAGF = -c -pedantic -Wall -W -O -fPIC#' makefile \
	&& sed -i 's#CFLAGX = -pedantic -Wall -W -O#CFLAGX = -pedantic -Wall -W -O -fPIC#' \
	&& make \
	&& make test \
	&& make install

RUN cd ~/repos \
	&& wget http://bitbucket.org/eigen/eigen/get/3.2.7.tar.gz \
	&& tar xfvz 3.2.7.tar.gz \
	&& cd ~/library/include \
	&& ln -s ~/repos/eigen-eigen-b30b87236a1b/Eigen/ Eigen

RUN cd ~/repos \
	&& wget http://www.netlib.org/lapack/lapack-3.6.0.tgz \
	&& wget http://downloads.sourceforge.net/project/math-atlas/Stable/3.10.2/atlas3.10.2.tar.bz2 \
	&& tar xfvj atlas3.10.2.tar.bz2 \
	&& mv ATLAS ATLAS3.10.2 \
	&& cd ATLAS3.10.2 \
	&& mkdir LINUX \
	&& cd LINUX \
	&& ../configure -b 64 --with-netlib-lapack-tarfile=/root/repos/lapack-3.6.0.tgz -D c -DWALL -Fa alg -fPIC --shared \
	&& sed -i 's#F77FLAGS = -O -mavx -fPIC -m64#F77FLAGS = -O -mavx -fPIC -m64 -frecursive#' interfaces/lapack/C2F/src/Make.inc \
	&& make build \
	&& make check \
	&& make time \
	&& make shared \
	&& make install 

RUN cd ~/repos \
	&& git clone https://bitbucket.org/jaredmales/mxlib.git \
	&& cd mxlib \
	&& sed -i 's#INSTALL_PATH = $(HOME)#INSTALL_PATH = $(HOME)/library#' Makefile \
	&& sed -i 's#BIN_PATH = $(HOME)/bin#BIN_PATH = $(HOME)/library/bin#' Makefile \
	&& sed -i 's#INCLUDE = -Iinclude -I$(HOME)/include#INCLUDE = -Iinclude -I$(HOME)/library/include#' Makefile \
	&& make \
	&& make install

RUN cd ~/repos \
	&& git clone https://bitbucket.org/jaredmales/acic.git \
	&& cd acic \
	&& sed -i 's#INCLUDE_PATH = $(HOME)/include#INCLUDE_PATH = $(HOME)/library/include#' makefile \
	&& sed -i 's#LIB_PATH = $(HOME)/lib#LIB_PATH = $(HOME)/library/lib#' makefile \
	&& sed -i 's?BOOST_PATH = /usr/local/lib?#BOOST_PATH = /usr/local/lib?' makefile \
	&& sed -i 's#MXLIB_EXLIBS = -lsofa_c -L/usr/lib64/ -lcfitsio -lrt -L$(BOOST_PATH) -lboost_system -lboost_filesystem $(GSL_LIBS) $(BLAS_LIBS) $(FFTW_LIBS)#MXLIB_EXLIBS = -lsofa_c -L/usr/lib64/ -lcfitsio -lrt -lboost_system -lboost_filesystem $(GSL_LIBS) $(BLAS_LIBS) $(FFTW_LIBS)#' makefile \
	&& make

RUN ln -s $HOME/repos/acic/darkmaster $HOME/library/bin/darkmaster \
	&& ln -s $HOME/repos/acic/darksub $HOME/library/bin/darksub \
	&& ln -s $HOME/repos/acic/fitscent $HOME/library/bin/fitscent \
	&& ln -s $HOME/repos/acic/klipReduce $HOME/library/bin/klipReduce

RUN cd ~/repos \
	&& wget http://ccl.cse.nd.edu/software/files/cctools-5.3.0-source.tar.gz && tar xfvz cctools-5.3.0-source.tar.gz && cd cctools-5.3.0-source \
	&& ./configure --prefix=$HOME/library \
	&& make \
	&& make install

RUN cd ~/repos \
	&& wget https://bootstrap.pypa.io/get-pip.py \
	&& python get-pip.py \
	&& pip install astropy

RUN cd ~/repos \
	&& git clone https://github.com/acic2015/findr.git

RUN cd ~/repos \
	&& rm *.tgz \
	&& rm *.bz2 \
	&& rm *.gz


























