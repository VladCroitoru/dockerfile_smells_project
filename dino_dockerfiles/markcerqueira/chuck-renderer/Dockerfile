FROM debian:jessie
MAINTAINER Mark Cerqueira <mark.cerqueira@gmail.com>

# ChucK dependencies
RUN apt-get update && apt-get install -y \
	build-essential \
	git \
	bison \
	flex \
	libsndfile1-dev \
	libpulse-dev \
	libasound2-dev
		
# Clone ChucK, build it, copy it to /bin/
RUN git clone --depth 1 https://github.com/ccrma/chuck.git \
	&& cd chuck/ \
	&& cd src/ \
	&& make linux-alsa \
	&& mv ./chuck /bin/
	
# libfdk-aac dependencies
RUN apt-get install -y \ 
	pkg-config \
	autoconf \
	automake \
	libtool \
	yasm

# Compile FDK AAC encoder - libfdk-aac
# https://trac.ffmpeg.org/wiki/CompilationGuide/Quick/libfdk-aac
RUN git clone --depth 1 https://github.com/mstorsjo/fdk-aac.git \
	&& cd fdk-aac \
	&& ./autogen.sh \
	&& ./configure --enable-shared --enable-static \
	&& make \
	&& make install
	
# Build FFMPEG with AAC encoder 
RUN git clone --depth 1 git://source.ffmpeg.org/ffmpeg.git \
	&& cd ffmpeg \ 
	&& ./configure --enable-libfdk-aac \
	&& make \
	&& make install
	
# RubyGems and sinatra/thin dependencies
RUN apt-get install -y \ 
	rubygems \
	ruby-dev
	
# Install sinatra and thin gems
RUN gem install \
	sinatra \
	thin

# Set Sinatra server as work directory
WORKDIR /server
COPY server .

# Expose port 9000 so we can access the server
EXPOSE 9000

# Run thin server
CMD ["thin", "-R", "config.ru", "-p", "9000", "start"]
