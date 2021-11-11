#
# docker run -it --rm=true \
# 	-e USER=$USER -e USERID=$UID \		# bind user for file permissions
#		-v /tmp/.X11-unix:/tmp/.X11-unix \ 	# mount the X11 socket
#		-e DISPLAY=unix$DISPLAY \ 			# pass the display
#		--device /dev/dri \
#		-v $HOME:/home/texmaker \			# mount $HOME
#		--name texmaker professormahi/texmaker-2017

FROM ubuntu:xenial
MAINTAINER Mahdi Fooladgar <mahdi.fooladgar@yahoo.com>
# Thanks to Julien Giovaresco <dev@giovaresco.fr>
# I've used the github repo https://github.com/jgiovaresco/dockerfiles

RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list

RUN apt-get update && apt-get upgrade -y  \
	&& apt-get install -y --no-install-recommends \
	software-properties-common \
	python-software-properties

RUN add-apt-repository ppa:jonathonf/texlive-2017 -y

RUN apt-get update && apt-get install -y --no-install-recommends \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	texmaker \
	texlive-generic-recommended \
	texlive-latex-recommended \
	texlive-fonts-recommended \
	texlive-extra-utils \
	texlive-font-utils \
	texlive-xetex \
	texlive-luatex \
	fonts-lmodern \
	fonts-font-awesome \
	wget \
	xzdec \
	unzip \
	&& apt-get autoclean -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

RUN useradd texmaker \
	&& mkdir /home/texmaker \
	&& chown texmaker:texmaker /home/texmaker

# Installing fonts
WORKDIR /tmp

RUN wget https://fontlibrary.org/assets/downloads/xb-zar/8e08f1d30a07e687d0a858558a852ce1/xb-zar.zip \
	--output-document=xb-zar.zip
RUN unzip xb-zar.zip
RUN mkdir -p /usr/share/fonts/truetype/XBZar
RUN mv 'Zar/XB Zar.ttf' /usr/share/fonts/truetype/XBZar/

RUN wget http://ftp.gnu.org/gnu/freefont/freefont-ttf-20060126.tar.gz \
	--output-document=gnu-fonts.tar.gz
RUN tar xvfz gnu-fonts.tar.gz
RUN mkdir -p /usr/share/fonts/truetype/GNUFonts/
RUN mv freefont-20060126/*.ttf /usr/share/fonts/truetype/GNUFonts/


# Install XePersian and bidi packeges
RUN tlmgr init-usertree
RUN tlmgr install xepersian && tlmgr install bidi

RUN cp -R /root/texmf/* /usr/share/texlive/texmf-dist/
RUN rm -rf /root/texmf/

RUN texhash


USER texmaker
WORKDIR /home/texmaker

ENTRYPOINT [ "texmaker" ]
