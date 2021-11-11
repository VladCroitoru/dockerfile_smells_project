# MagicLantern Build Environment

FROM ubuntu:17.04
MAINTAINER matteopic

RUN apt-get update && \
    apt-get install mercurial sudo wget -yq && \
	cd /usr/src && \ 
	hg clone -u unified https://bitbucket.org/shadowfax/magic-lantern

RUN apt-get install build-essential less bzip2 lib32ncurses5 -yq && \
    cd /tmp && \
    wget --no-verbose https://launchpad.net/gcc-arm-embedded/4.8/4.8-2013-q4-major/+download/gcc-arm-none-eabi-4_8-2013q4-20131204-linux.tar.bz2 && \
	tar -xvjf gcc-arm-none-eabi-4_8-2013q4-20131204-linux.tar.bz2 && \
	mv gcc-arm-none-eabi-4_8-2013q4 ~/gcc-arm-none-eabi-4_8-2013q4


	
	
# Avoid CPAN prompt for confirmation
ENV PERL_MM_USE_DEFAULT=1
ENV PERL_EXTUTILS_AUTOINSTALL="--defaultdeps"

RUN apt-get install perl python -yq && \
    perl -MCPAN -e 'install File::Slurp'

	
	

# Build documents dependencies
RUN apt-get install doxygen -yq	

RUN apt-get install zip nano -yq	




# disassemble.pl from http://chdk.wikia.com/wiki/GPL:disassemble.pl
ADD disassemble.pl /usr/bin

# Patch from http://www.magiclantern.fm/forum/index.php?topic=12177.0
ADD disassemble.pl.patch /tmp

RUN patch /usr/bin/disassemble.pl /tmp/disassemble.pl.patch && \
    chmod 744 /usr/bin/disassemble.pl

	
	

# Compile QEMU environment
RUN apt-get install pkg-config zlib1g zlib1g-dev libsdl-image1.2-dev bison flex autoconf -yq

RUN cd /usr/src/magic-lantern/contrib/qemu && \
    echo Y | ./install.sh && \
	cd /usr/src/qemu/qemu-1.6.0 && \
	./configure --target-list=arm-softmmu --disable-docs --enable-sdl
	
