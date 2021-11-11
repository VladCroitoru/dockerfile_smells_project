# ffmpeg build - simply change versions to compile
# This Dockerfile is based on docker image  rottenberg/ffmpeg
# The purpose behind this is to build ffmpeg inside a debian container.
# 	Then the next step is to export the compiled binaries into an untouched base debian image
# 	This results in a ~50% images size reduction.
# 	FYI:  this image is useable....I just like having a smaller base image to download.
# Some of these options I don't use, so I commented them out.
# My builds include only FFMPEG + libfdk_aac + libmp3lame+ latest x264 + Decklink(Blackmagic)
# I am including Decklink(Blackmagic) so I can utilize those devices
# I don't need anything else.  If you need anything included, email me and I can make alternative builds.
# I will be tracking the 'stable' rolling release of Debian
# I am using Debian Jessie for now, until I upgrade my current machine, since it needs the older glibc

FROM		debian:jessie
MAINTAINER	Nachochip <blockchaincolony@gmail.com>


ENV	YASM_VERSION    	1.3.0
	# monitor releases at https://github.com/yasm/yasm/releases
ENV	NASM_VERSION    	2.14.02
	# monitor releases at https://www.nasm.us
ENV	FDKAAC_VERSION  	0.1.6
	# due to API changes, don't use v2.0.1 just yet, perhaps a higher ffmpeg version
	# monitor releases at https://github.com/mstorsjo/fdk-aac/releases
#ENV	x264
	# this project does not use release versions at this time
	# monitor project at http://git.videolan.org/?p=x264.git;a=shortlog
ENV	LAME_VERSION    	3.100
	# monitor releases at https://sourceforge.net/projects/lame/rss?path=/lame
ENV	BLACKMAGIC_SDK_VERSION	10.11.2
	# 10.8.3 older ones vs 10.9.5 newer ones
	# v 10.11.2 is current one
	# monitor my own releases at https://github.com/nachochip/Blackmagic-SDK/releases
	# the origin of the drivers comes from https://www.blackmagicdesign.com/support/family/capture-and-playback
	# I roll them into github to track it better, and condense to only linux-drivers
ENV	SRC             	/usr/local
ENV	LD_LIBRARY_PATH 	${SRC}/lib
ENV	PKG_CONFIG_PATH 	${SRC}/lib/pkgconfig
ENV	INSTALL_PACKAGES	"autoconf automake gcc build-essential git libtool make zlib1g-dev tar curl"


RUN bash -c 'set -euo pipefail'
RUN apt-get update
RUN apt-get install -y ${INSTALL_PACKAGES}

# YASM
# REMOVE THIS SECTION????????????????????
RUN DIR=$(mktemp -d) && cd ${DIR} && \
		curl -O http://www.tortall.net/projects/yasm/releases/yasm-${YASM_VERSION}.tar.gz && \
		tar xzvf yasm-${YASM_VERSION}.tar.gz && \
		cd yasm-${YASM_VERSION} && \
		./configure --prefix="$SRC" --bindir="${SRC}/bin" && \
		make -j$(nproc) && \
		make install && \
		make distclean && \
		rm -rf ${DIR}

# NASM
RUN DIR=$(mktemp -d) && cd ${DIR} && \
		curl -O https://www.nasm.us/pub/nasm/releasebuilds/${NASM_VERSION}/nasm-${NASM_VERSION}.tar.bz2 && \
		tar xjvf nasm-${NASM_VERSION}.tar.bz2 && \
		cd nasm-${NASM_VERSION} && \
		./autogen.sh && \
		PATH="$SRC/bin:$PATH" ./configure --prefix="${SRC}" --bindir="${SRC}/bin" && \
		make -j$(nproc )&& \
		make install

# x264
RUN DIR=$(mktemp -d) && cd ${DIR} && \
		git -C x264 pull 2> /dev/null || git clone --depth 1 https://code.videolan.org/videolan/x264.git && \
		cd x264 && \
		./configure --prefix="$SRC" --bindir="${SRC}/bin" --enable-static --enable-pic --disable-opencl && \
		make -j$(nproc) && \
		make install && \
		make distclean && \
		rm -rf ${DIR}

# LAME
RUN DIR=$(mktemp -d) && cd ${DIR} && \
		curl -LOs http://downloads.sourceforge.net/project/lame/lame/${LAME_VERSION}/lame-${LAME_VERSION}.tar.gz && \
		tar xzvf lame-${LAME_VERSION}.tar.gz && \
		cd lame-${LAME_VERSION} && \
		./configure --prefix="${SRC}" --bindir="${SRC}/bin" --disable-shared --enable-nasm && \
		make -j$(nproc) && \
		make install && \
		make distclean && \
		rm -rf ${DIR}

# FDK_AAC
RUN DIR=$(mktemp -d) && cd ${DIR} && \
              curl -s https://codeload.github.com/mstorsjo/fdk-aac/tar.gz/v${FDKAAC_VERSION} | tar zxvf - && \
              cd fdk-aac-${FDKAAC_VERSION} && \
              autoreconf -fiv && \
              ./configure --prefix="${SRC}" --disable-shared && \
	      make -j$(nproc) && \
              make install && \
              make distclean && \
              rm -rf ${DIR}

# Blackmagic SDK
RUN cd /usr/src/ && \
	      curl -s https://codeload.github.com/nachochip/Blackmagic-SDK/tar.gz/${BLACKMAGIC_SDK_VERSION} | tar xzvf -

# ============================================
# For Debian:Jessie, I have to disable this part, once I run a newer debian, I can enable AV1
# Due to GCC-5.4 is in newer versions and other reasons
# !! DON'T forget to enable-libaom below

# Cmake, in future, will be different
# Debian:Jessie has an old cmake version, so i am compiling a current version for now
# this is here because I am adding the AV1 codec which needs cmake

#  !!AV1 below needs openssl, python, cmake, and GCC-5.4????  So maybe not with Debian:Jessie!!!
#RUN 	apt-get install -y openssl libssl-dev python
#RUN DIR=$(mktemp -d) && cd ${DIR} && \
#	curl -OL https://github.com/Kitware/CMake/releases/download/v3.16.3/cmake-3.16.3.tar.gz && \
#	tar xzvf cmake-3.16*.tar.gz && \
#	cd cmake* && \
#	./bootstrap && \
#	make -j$(nproc)	&& \
#	make install && \
#       rm -rf ${DIR}

# AV1 codec
# working on this right now!!!!!!!!!!!!!!!!!!
#RUN DIR=$(mktemp -d) && cd ${DIR} && \
#	git -C aom pull 2> /dev/null || git clone --depth 1 https://aomedia.googlesource.com/aom && \
#	mkdir -p aom_build && \
#	cd aom_build && \
#	PATH="${SRC}/bin:$PATH" cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="${SRC}" -DENABLE_SHARED=off -DENABLE_NASM=on ../aom && \
#	PATH="${SRC}/bin:$PATH" make -j$(nproc) && \
#	make install && \
#	rm -rf ${DIR}
# ============================================

# This is remnants for enabling screenshot, but rpi will need arm, not x86.
# for specific requirements, look at "Copmilation Guide Ubuntu"  there are some dependencies
# I have not written them down here, because I'm pushing this part aside for now
#RUN apt-get install -y libavcodec-dev libxcb1-dev libxcb-util0-dev libxcb* libx11*
#RUN apt-get install -y x11* libx11*
#  Im trying to get x11grab or libxcb inputted in ffmpegv3.3 and after, I can always track it back later.
# main goal was to get rpi with this, but I don't want to cross-compile at this time since this is for x86
# ============================================


# !! Working on this now !!
ENV	FFMPEG_VERSION		4.2.2
	# monitor releases at https://github.com/FFmpeg/FFmpeg/releases
	# 4.2-.2 works, no fails
	# 4.1-.5 works, no fails
	# 4.0-.5 works, no fails
	# 3.5 line does not exist
	# 3.4.2-7 works, 3.4.1 fails
	# 3.3.6-9 works, 3.3.5 fails
	# 3.2.10-14 works, 3.2.9 fails
	# 3.2.4 was last one released by nachochip, next to release is 3.2.5, but error in x264/ffmpeg
	# I'm not working on anything before this
	# 3.0.10 fails
	# 2.4.14 fails, 12-31-2017, anything after works (was from some x264/ffmpeg issue)
	# Can use newer Blackmagic drivers after 4.2.1 i think
	# BM driver  >=10.9.5 for newer FFMPEG
	# Current BM Driver on computer is 10.11.2

# FFMPEG
# I don't use these in my configure: --enable-x11grab --enable-libxcb --enable-libaom
RUN DIR=$(mktemp -d) && cd ${DIR} && \
		curl -Os http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz && \
		tar xzvf ffmpeg-${FFMPEG_VERSION}.tar.gz && \
		cd ffmpeg-${FFMPEG_VERSION} && \
		./configure --prefix="${SRC}" --extra-cflags="-I${SRC}/include" --extra-ldflags="-L${SRC}/lib" --bindir="${SRC}/bin" \
		--extra-libs="-lpthread -lm" --enable-version3 --enable-libx264 --enable-gpl \
		--enable-postproc --enable-nonfree --enable-avresample --enable-libfdk_aac --disable-debug --enable-small \
		--enable-libmp3lame \
		--enable-decklink --extra-cflags=-I/usr/src/Blackmagic-SDK-${BLACKMAGIC_SDK_VERSION}/Linux/include/ \
		--extra-ldflags=-L/usr/src/Blackmagic-SDK-${BLACKMAGIC_SDK_VERSION}/Linux/include/ && \
		make -j$(nproc) && \
		make install && \
		make distclean && \
		hash -r && \
		rm -rf ${DIR}

# This is not really needed, because I don't compress the image, I only extract what I need
#RUN apt-get purge -y ${INSTALL_PACKAGES}
#RUN apt-get clean
#RUN apt-get autoclean

RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/libc.conf

CMD           ["--help"]
ENTRYPOINT    ["ffmpeg"]
