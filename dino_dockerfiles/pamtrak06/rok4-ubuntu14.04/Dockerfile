FROM ubuntu:14.04

# installation instructions from http://www.rok4.org/documentation/rok4-installation

# update os and install utilities
RUN apt-get update && apt-get install -y wget unzip

# Install mapcache compilation prerequisites
#RUN apt-get install -y software-properties-common g++ make cmake
RUN apt-get install -y build-essential

# install libraries compilation prerequisites
RUN apt-get install -y gettext nasm libturbojpeg automake

# install libraries BE4 prerequisites
RUN apt-get install -y perl libxml2-dev libgdal-perl 

# install perl libraries

#RUN cpan prompt &gt; install Log::Log4perl
#RUN cpan prompt &gt; install Config::IniFiles
#RUN cpan prompt &gt; install File::Spec::Linkexit

RUN apt-get install -y liblog-log4perl-perl libconfig-inifiles-perl libxml-libxml-simple-perl libfile-copy-link-perl

# install documentation libraries
RUN apt-get install -y doxygen graphviz naturaldocs

# install cmake
RUN apt-get install -y cmake 

# download and install rok4 latest sources
RUN wget http://www.rok4.org/data/src/rok4-0.19.0-src.zip
RUN unzip rok4-0.19.0-src.zip

# rok4 compilation
RUN cd rok4-*; mkdir build; cd build; \
	cmake .. -DCMAKE_INSTALL_PREFIX=/opt/rok4; \
	make; \
	make doc; \
	make install

# install apache2 with Mod_fcgid enabled
RUN apt-get install -y apache2 libapache2-mod-fcgid
RUN a2enmod fcgid


EXPOSE 22
EXPOSE 80

# run apache (rok4 start : /opt/rok4/bin/rok4)
CMD [apache2ctl start]


