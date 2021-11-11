#
# GROMED : GRO[macs] + [plu]MED
#
# For many reasons we need to fix the ubuntu release,
# this version underwent the apt update; apt upgrade ; apt install ..
# torture 
FROM 	rinnocente/ubuntu-17.04-homebrewed
#
LABEL 	\
	maintainer="roberto innocente <inno@sissa.it>" \
	version="1.0"
#
#
ARG \
	DEBIAN_FRONTEND=noninteractive
#
# Automatic builds on docker cloud cant compile all these
# versions. We leave only SSE2
#ARG GR_SIMD="None SSE2 SSE4.1 AVX_256 AVX2_256 AVX_512"
ARG \ 
	GR_SIMD="SSE2"
#
# we create the user 'gromed' and add it to the list of sudoers
RUN  \
	adduser -q --disabled-password --gecos gromed gromed  \
	&& printf "\ngromed ALL=(ALL:ALL) NOPASSWD:ALL" >>/etc/sudoers.d/gromed  \
	&& (echo "gromed:mammamia"|chpasswd)
#
# disable  ssh strict mode
#
RUN \
	sed -i 's#^StrictModes.*#StrictModes no#' /etc/ssh/sshd_config \
	&& service   ssh  restart  
#
# download and compile sources.
#
ENV     GR_HD="/home/gromed" \
   	GR_VER="-2016.3" \
   	PL_VER="-2.3.1"  
#
WORKDIR "$GR_HD"
#
# First : setup PLUMED
# Second : setup GROMACS
#
RUN     \
	GR_CORES=$(grep 'cpu cores' /proc/cpuinfo |uniq|sed -e 's/.*://') \
	&& wget http://people.sissa.it/~inno/plumed"${PL_VER}".tgz  \
	&& tar xfz plumed"${PL_VER}".tgz \
	&& ( cd plumed"${PL_VER}" || exit ; \
	       ./configure CXXFLAGS=-O3; \
	       make -j $((2*GR_CORES)) ;\
               make install ) \
	&& wget http://ftp.gromacs.org/pub/gromacs/gromacs"${GR_VER}".tar.gz \
	&& tar xfz gromacs"${GR_VER}".tar.gz \
	&& ( cd gromacs"${GR_VER}" ; \
	        plumed patch -p -e gromacs"${GR_VER}" ; \
	        for item in $GR_SIMD; do \
		     mkdir -p build-"$item" ; \
		     (cd build-"$item"; cmake .. \
			 -DGMX_SIMD="$item" -DCMAKE_C_COMPILER=mpicc -DCMAKE_CXX_COMPILER=mpicxx  \
			 -DGMX_THREAD_MPI:BOOL=OFF -DGMX_MPI:BOOL=ON ; make -j $((2*GR_CORES)) ); \
	        done ;\
	        (cd build-SSE2; make install)) \
	&&  echo export PATH=/usr/local/gromacs/bin:"${PATH}" >>"${GR_HD}"/.bashrc \
	&&  echo "source /usr/local/gromacs/bin/GMXRC" >>"${GR_HD}"/.bashrc

#
# move tarballs in downloads/ directory
#
RUN    \
	mkdir downloads \
	&& mv gromacs"${GR_VER}".tar.gz downloads/
#
COPY	tune-gromacs.sh "${GR_HD}"/gromacs"${GR_VER}"/
#
# change owner to gromed:gromed
#
RUN	chown -R gromed:gromed /home/gromed
#
#
EXPOSE 22
#
USER gromed
#
# the container can be now reached via ssh
CMD [ "sudo","/usr/sbin/sshd","-D" ]

