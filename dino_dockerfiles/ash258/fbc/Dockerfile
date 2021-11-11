FROM debian as Freebasic

# Required by Freebasic
# @see https://freebasic.net/wiki/DevBuildLinux
# sudo apt install gcc make lib{ncurses5,gpm,x11,xext,xpm,xrandr,xrender,gl1-mesa,ffi}-dev
# sudo apt-get install gcc make lib{ncurses5,gpm,x11,xext,xpm,xrandr,xrender,gl1-mesa,ffi}-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3 \
	wget \
	bzip2 \
	ca-certificates \
	gcc \
	make \
	valgrind \
	unzip \
	zip \
	libffi-dev \
	libgl1-mesa-dev \
	libgpm-dev \
	libncurses5-dev \
	libx11-dev \
	libxext-dev \
	libxpm-dev \
	libxrandr-dev \
	libxrender-dev

COPY ./FreeBASIC-1.05.0-linux-x86_64.tar.gz \
	./Criterion-v2.3.2-linux-x86_64.tar.bz2 \
	./ic17int_linux64_2017-11-24.zip \
	/usr/local/

# Freebasic, Criterion, ic17int
RUN cd /usr/local/ \
	&& tar -xf FreeBASIC-1.05.0-linux-x86_64.tar.gz \
	&& cd ./FreeBASIC-1.05.0-linux-x86_64 \
	&& ./install.sh -i \
	&& cd .. \
	&& tar -xjf Criterion-v2.3.2-linux-x86_64.tar.bz2 \
	&& cd criterion-v2.3.2 \
	&& cp -r * /usr/ \
	&& cd .. \
	&& unzip ./ic17int_linux64_2017-11-24.zip -d ./ic17int_linux64_2017-11-24 \
	&& cp ./ic17int_linux64_2017-11-24/ic17int /usr/bin/ \
	&& chmod +x /usr/bin/ic17int

# Final cleaning => Significantly reduce image size
RUN apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& cd /usr/local/ \
	&& rm -rf ./criterion-v2.3.2 \
	./Criterion-v2.3.2-linux-x86_64.tar.bz2 \
	./FreeBASIC-1.05.0-linux-x86_64 \
	./FreeBASIC-1.05.0-linux-x86_64.tar.gz \
	ic17int_linux64_2017-11-24 \
	ic17int_linux64_2017-11-24.zip

CMD [ "tail", "-f", "/dev/null" ]
