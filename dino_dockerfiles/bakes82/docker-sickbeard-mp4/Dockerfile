FROM ubuntu:16.04
#Based on the work of Eric Schultz <eric@startuperic.com>
#Thanks to Tim Haak <tim@haak.co.uk>
#ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root
WORKDIR /work

RUN locale-gen en_US en_US.UTF-8

# Use baseimage-dockers init system
CMD ["/sbin/my_init"]

RUN apt-get -q update --fix-missing
RUN apt-get -qy upgrade

# Supervisor
RUN apt-get -qy install supervisor

## Dependencies
RUN apt-get -qy install python wget git autoconf automake build-essential libass-dev libfreetype6-dev 
RUN	apt-get -qy install libgpac-dev libsdl1.2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev 
RUN	apt-get -qy install libx11-dev libxext-dev libxfixes-dev pkg-config texi2html zlib1g-dev yasm libx264-dev 
Run apt-get -qy install libmp3lame-dev libopus-dev unzip

# Install FFMPEG
## Dep. libfdk-aac
RUN	git clone git://github.com/mstorsjo/fdk-aac.git fdk-aac

WORKDIR /work/fdk-aac
RUN autoreconf -fiv 
RUN	./configure --prefix="$HOME/ffmpeg_build" --disable-shared  
RUN	make  
RUN	make install  
RUN	make distclean

## FFMPEG Source
WORKDIR /work
RUN git clone https://github.com/FFmpeg/FFmpeg ffmpeg-source

WORKDIR /work/ffmpeg-source
RUN PATH="$PATH:$HOME/bin" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure \
	  --prefix="$HOME/ffmpeg_build" \
	  --extra-cflags="-I$HOME/ffmpeg_build/include" \ 
	  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
	  --bindir="$HOME/bin" \
	  --enable-gpl \
	  --enable-libass \ 
	  --enable-libfdk-aac \
	  --enable-libfreetype \ 
	  --enable-libmp3lame \
	  --enable-libopus \
	  --enable-libtheora \
	  --enable-libvorbis \
	  --enable-libx264 \
	  --enable-nonfree  
RUN PATH="$PATH:$HOME/bin" make  
RUN	make install  
RUN	make distclean  
RUN	hash -r

WORKDIR /work

## Python Setup Tools
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python

## PIP
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

RUN pip install requests
##RUN pip install requests[security]
RUN pip install requests-cache
RUN pip install babelfish
RUN pip install "guessit<2"
RUN pip install "subliminal<2"
RUN pip install qtfaststart

## MP4 Automator
RUN git clone git://github.com/mdhiggins/sickbeard_mp4_automator.git mp4_automator
COPY autoProcess.ini /work/mp4_automator/autoProcess.ini

COPY job.sh /work/
RUN chmod 0777 /work/job.sh

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/mp4automator-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/mp4automator-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

#Install Cron
RUN apt-get update
RUN apt-get -y install cron

RUN crontab -u root /etc/cron.d/mp4automator-cron

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

RUN service cron start

# Install Configs
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /work/supervisord.conf


VOLUME ["/config", "/storage", "/incoming"]

CMD [ "-c", "/work/supervisord.conf"]
ENTRYPOINT ["/usr/bin/supervisord"]
