FROM ubuntu:latest

LABEL maintainer="michel@michel.eti.br"

# change repository for performance and enable other packages
RUN mv /etc/apt/sources.list /etc/apt/sources.list.backup \
 	&& sed \
	-e 's#deb http://archive.ubuntu.com/ubuntu/ xenial universe#deb http://archive.ubuntu.com/ubuntu/ xenial universe#g' \
	-e 's#deb http://archive.ubuntu.com/ubuntu/ xenial-updates universe#deb http://archive.ubuntu.com/ubuntu/ xenial-updates universe#g' \
	-e 's#deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates universe#deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates universe#g' \
	-e 's#deb-src http://archive.ubuntu.com/ubuntu/ xenial universe#deb-src http://archive.ubuntu.com/ubuntu/ xenial universe#g' \
	-e 's#\# deb http://archive.ubuntu.com/ubuntu/ xenial-security multiverse#deb http://archive.ubuntu.com/ubuntu/ xenial-security#g' \
	-e 's#\# deb-src http://archive.ubuntu.com/ubuntu/ xenial-security multiverse#deb-src http://archive.ubuntu.com/ubuntu/ xenial-security#g' \
	-e 's#archive.ubuntu.com#br.archive.ubuntu.com#g' /etc/apt/sources.list.backup > /etc/apt/sources.list


# install PHP extensions that are needed
RUN apt-get update && apt-get install -y software-properties-common python-software-properties imagemagick build-essential \
	subversion git-core checkinstall texi2html libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev \
	libtheora-dev libvorbis-dev libx11-dev libxfixes-dev libxvidcore-dev zlib1g-dev libavcodec-dev nasm yasm libfaac0 \
	dcraw ufraw gpac unzip\
	&& apt-add-repository -y ppa:webupd8team/java \
	&& apt-get update -y \
	&& apt-get clean

# install Oracle with it's lovelly license process
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections \
	&& echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections \
	&& apt-get install -y oracle-java8-installer \
	&& rm -rf /var/lib/apt/lists/* 

# install x264 codec
RUN cd /opt && git clone --depth=1 git://git.videolan.org/x264.git && cd x264 \
	&& ./configure --enable-static --disable-opencl --disable-asm && make \
	&& checkinstall --pkgname=x264 --default --backup=no --deldoc=yes --fstrans=no --pkgversion=3.4.5 \
	&& cd ../ && rm -rf x264

# install lame
RUN cd /opt && wget -nv http://downloads.sourceforge.net/project/lame/lame/3.98.4/lame-3.98.4.tar.gz \
	&& tar xzvf lame-3.98.4.tar.gz && cd lame-3.98.4 \
	&& ./configure --enable-nasm --disable-shared \
	&& make \
	&& checkinstall --pkgname=lame-ffmpeg --pkgversion="3.98.4" --backup=no --default --deldoc=yes \
	&& cd ../ && rm -rf lame-3.98.4

# install libvpx
RUN cd /opt && git clone --depth=1 https://chromium.googlesource.com/webm/libvpx.git \
	&& cd libvpx \
	&& ./configure \
	&& make \
	&& checkinstall --pkgname=libvpx --pkgversion="`date +%Y%m%d%H%M`-git" --backup=no \
		--default --deldoc=yes \
	&& cd ../ && rm -rf libvpx

# install ffmpeg
RUN cd /opt && git clone --depth=1 git://source.ffmpeg.org/ffmpeg.git && cd ffmpeg \
	&& ./configure --enable-gpl --enable-version3 --enable-nonfree --enable-postproc \
		--enable-libopencore-amrnb --enable-libopencore-amrwb \
		--enable-libtheora --enable-libvorbis --enable-libx264 --enable-libxvid \
		--enable-libvpx --enable-libmp3lame \
	&& make \
	&& checkinstall --pkgname=ffmpeg --pkgversion=`./version.sh | sed -e "s#git-##g"` --backup=no --deldoc=yes --default \
	&& cd ../ && rm -rf ffmpeg

# install Exiftool
RUN cd /opt && wget -nv -c "https://downloads.sourceforge.net/project/exiftool/Image-ExifTool-10.61.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fexiftool%2Ffiles%2F%3Fsource%3Dnavbar&ts=1506268522&use_mirror=ufpr" -O "Image-ExifTool-10.61.tar.gz" \
	&& gzip -dc Image-ExifTool-10.61.tar.gz | tar -xf - && cd Image-ExifTool-10.61  \
	&& perl Makefile.PL && make install \
	&& cd ../ && rm -rf Image-ExifTool-10.61

# install Ghost Script
#RUN cd /opt && wget -nv http://downloads.ghostscript.com/public/binaries/ghostscript-9.15-linux-x86_64.tgz \
#	&& tar xzvf ghostscript-9.15-linux-x86_64.tgz \
#	&& cd /usr/bin/ \
#	&& ln -s /opt/ghostscript-9.15-linux-x86_64/gs-915-linux_x86_64 gs

#configure Java home variable
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle

# install razuna
RUN cd /opt && wget -nv http://cloud.razuna.com/installers/1.9.1/razuna_tomcat_1_9_1.zip \
	&& unzip -q razuna_tomcat_1_9_1.zip && mv razuna_tomcat_1_9_1 razuna \
	&& rm razuna_tomcat_1_9_1.zip

EXPOSE 8080

WORKDIR /opt/razuna/tomcat/bin
CMD ["./catalina.sh", "run"]
