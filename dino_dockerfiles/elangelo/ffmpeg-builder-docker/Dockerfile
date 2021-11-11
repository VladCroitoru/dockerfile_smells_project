FROM ubuntu:16.04

RUN apt update
RUN apt install -y \
	texinfo \
	pax \
	bzip2 \
	make \
	gcc \
	wget \
	pax \
	cvs \
	git \
	yasm \
	subversion \
	cmake \
	xz-utils \
	g++ \
	flex \
	m4 \
	bison \
	autoconf \
	automake \
	build-essential \
	libass-dev \
	libfreetype6-dev \
	libsdl1.2-dev \
	libtheora-dev \
	libtool \
	libva-dev \
	libvorbis-dev \
	pkg-config \
	nasm \
	unzip \
	mercurial \
	ed \
	curl

RUN apt install -y vim

RUN mkdir compile

#ADD http://zeranoe.com/scripts/mingw_w64_build/mingw-w64-build-3.6.7 /home/compile-user/source/mingw-w64-build-3.6.7
#COPY mingw-w64-build-3.6.7 /compile/mingw-w64-build-3.6.7
#RUN chmod +x /compile/mingw-w64-build-3.6.7
#RUN /compile/mingw-w64-build-3.6.7 --build-type=win64 --cpu-count=4 --default-configure
VOLUME /result
WORKDIR compile

#RUN git clone https://github.com/rdp/ffmpeg-windows-build-helpers
#RUN git clone https://github.com/DeadSix27/ffmpeg-windows-build-helpers

COPY entrypoint.sh /compile
RUN chmod +x /compile/entrypoint.sh

CMD [ "/compile/entrypoint.sh" ]
